"""
Device Communication Module.

This module handles all communication with your device. It manages connections,
sends commands, and tracks the device state.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import asyncio
import logging

from stormaudio import StormAudioClient

import json
from typing import Any, Dict

from ucapi import EntityTypes
from ucapi.media_player import States, Attributes as MediaAttr
from ucapi_framework import PersistentConnectionDevice, create_entity_id
from ucapi_framework.device import DeviceEvents

from const import StormAudioCommands, StormAudioResponses

_LOG = logging.getLogger(__name__)

MIN_VOLUME = 0
MAX_VOLUME = 100
MAX_TIME_OUT = 20


class StormAudioDevice(PersistentConnectionDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._waiters: list[tuple[str, asyncio.Future[str]]] = []
        self._state = States.UNKNOWN
        self._source_list = self.device_config.input_list
        self._sound_mode_list = {
            "Native": 0,
            "Stereo Downmix": 1,
            "Dolby Surround": 2,
            "DTS Neural:X": 3,
            "Auro-Matic": 4,
        }
        self._volume: int = 40
        self._client = StormAudioClient(self.address, self.device_config.port)

    @property
    def state(self) -> States:
        """Return the current device state."""
        return self._state

    @property
    def source_list(self) -> Dict[str, int]:
        """Returns a dictionary of available input sources."""
        return self._source_list

    @property
    def volume(self) -> int:
        """Returns the current device volume."""
        return self._volume

    @property
    def sound_mode_list(self) -> Dict[str, int]:
        """Returns a dictionary of available sound modes."""
        return self._sound_mode_list

    @property
    def identifier(self) -> str:
        """Return the device identifier."""
        return self._device_config.identifier

    @property
    def name(self) -> str:
        """Return the device name."""
        return self._device_config.name

    @property
    def address(self) -> str | None:
        """Return the device address."""
        return self._device_config.address

    @property
    def log_id(self) -> str:
        """Return a log identifier for debugging."""
        return self.name if self.name else self.identifier

    @property
    def entity_id(self) -> str:
        """Returns the unique entity-ID."""
        return create_entity_id(EntityTypes.MEDIA_PLAYER, self.identifier)

    async def establish_connection(self) -> Any:
        return await self._client.connect()

    async def close_connection(self) -> None:
        if self._connection:
            await self._client.close(self._connection)

    async def maintain_connection(self) -> None:
        def message_handler(message: str) -> None:
            match message:
                case StormAudioResponses.PROC_STATE_ON:
                    self._state = States.ON
                    self._update_attributes()
                case (
                    StormAudioResponses.PROC_STATE_OFF
                    | StormAudioResponses.PROC_STATE_INDETERMINATE
                ):
                    # Maps both the initialization and the process of shutting down to OFF
                    # as they are not "fully booted"
                    self._state = States.OFF
                    self._update_attributes()
                case StormAudioResponses.MUTE_ON | StormAudioResponses.MUTE_OFF:
                    self.events.emit(
                        DeviceEvents.UPDATE,
                        self.entity_id,
                        {
                            MediaAttr.MUTED: True
                            if message == StormAudioResponses.MUTE_ON
                            else False
                        },
                    )
                case message if message.startswith(StormAudioResponses.VOLUME_X):
                    # The UC remotes currently only support relative volume scales.
                    # That's why we need to convert the absolute values from the ISPs.
                    self._volume = (
                        int(float(message[len(StormAudioResponses.VOLUME_X) : -1]))
                        + MAX_VOLUME
                    )
                    self._update_attributes()
                case message if message.startswith(StormAudioResponses.INPUT_LIST_X):
                    input_name, input_id, *tail = json.loads(
                        message[len(StormAudioResponses.INPUT_LIST_X) :]
                    )

                    self._source_list.update({input_name: input_id})
                    self._update_attributes()

        await self._client.parse_response_messages(self._connection, message_handler)

    async def _send_command(self, command: str) -> None:
        """Send a command to the device."""
        if not self._connection:
            _LOG.error("[%s] Cannot send command, not connected", self.log_id)
            return

        await self._client.send_command(self._connection, command)

    async def _wait_for_response(
        self, pattern: str, timeout: float = 5.0
    ) -> str | None:
        await self._client.wait_for_response(pattern, timeout)

    def _update_attributes(self) -> None:
        """Update the device attributes via an event."""
        self.events.emit(
            DeviceEvents.UPDATE,
            self.entity_id,
            {
                MediaAttr.STATE: self._state,
                MediaAttr.SOURCE_LIST: list(self.source_list.keys()),
                MediaAttr.SOUND_MODE_LIST: list(self.sound_mode_list.keys()),
                MediaAttr.VOLUME: self.volume,
            },
        )

    async def power_on(self):
        """Power on the StormAudio processor."""
        await self._send_command(StormAudioCommands.POWER_ON)
        await self._send_command(StormAudioCommands.PROC_STATE)
        await self._wait_for_response(StormAudioResponses.PROC_STATE_ON, MAX_TIME_OUT)

    async def power_off(self):
        """Power off the StormAudio processor."""
        await self._send_command(StormAudioCommands.POWER_OFF)
        await self._send_command(StormAudioCommands.PROC_STATE)
        await self._wait_for_response(StormAudioResponses.PROC_STATE_OFF)

    async def power_toggle(self):
        """Toggle the power of the StormAudio processor."""
        current_power_state = self.state

        await self._send_command(StormAudioCommands.POWER_TOGGLE)
        await self._send_command(StormAudioCommands.PROC_STATE)

        if current_power_state == States.ON:
            await self._wait_for_response(StormAudioResponses.PROC_STATE_OFF)
        else:
            await self._wait_for_response(
                StormAudioResponses.PROC_STATE_ON, MAX_TIME_OUT
            )

    async def mute_on(self):
        """Mute the StormAudio processor."""
        await self._send_command(StormAudioCommands.MUTE_ON)
        await self._wait_for_response(StormAudioResponses.MUTE_ON)

    async def mute_off(self):
        """Unmute the StormAudio processor."""
        await self._send_command(StormAudioCommands.MUTE_OFF)
        await self._wait_for_response(StormAudioResponses.MUTE_OFF)

    async def mute_toggle(self):
        """Toggle mute of the StormAudio processor."""
        await self._send_command(StormAudioCommands.MUTE_TOGGLE)

    async def volume_x(self, volume):
        # The UC remotes only support relative volume scales for now.
        # That's why we need to convert the absolute values from the ISPs.
        sanitized_volume = max(MIN_VOLUME, min(MAX_VOLUME, int(volume)))
        absolute_volume = sanitized_volume - MAX_VOLUME
        await self._send_command(StormAudioCommands.VOLUME_X.format(absolute_volume))
        await self._wait_for_response(
            StormAudioCommands.VOLUME_X.format(sanitized_volume)
        )

    async def volume_up(self):
        """Increase the volume of the StormAudio processor by 1dB."""
        target_volume = float(self.volume - MAX_VOLUME + 1)

        await self._send_command(StormAudioCommands.VOLUME_UP)
        await self._wait_for_response(StormAudioCommands.VOLUME_X.format(target_volume))

    async def volume_down(self):
        """Decrease the volume of the StormAudio processor by 1dB."""
        target_volume = float(self.volume - MAX_VOLUME - 1)

        await self._send_command(StormAudioCommands.VOLUME_DOWN)
        await self._wait_for_response(StormAudioCommands.VOLUME_X.format(target_volume))

    async def select_source(self, source):
        """Select the input of the StormAudio processor."""
        await self._send_command(
            StormAudioCommands.INPUT_X.format(self.source_list.get(source))
        )
        await self._wait_for_response(
            StormAudioResponses.INPUT_X.format(self.source_list.get(source))
        )

    async def select_sound_mode(self, mode):
        """Set the surround mode of the StormAudio processor."""
        await self._send_command(
            StormAudioCommands.SURROUND_MODE_X.format(self.sound_mode_list.get(mode))
        )

    async def cursor_up(self):
        await self._send_command(StormAudioCommands.NAV_UP)
        await self._wait_for_response(StormAudioResponses.NAV_UP)

    async def cursor_down(self):
        await self._send_command(StormAudioCommands.NAV_DOWN)
        await self._wait_for_response(StormAudioResponses.NAV_DOWN)

    async def cursor_left(self):
        await self._send_command(StormAudioCommands.NAV_LEFT)
        await self._wait_for_response(StormAudioResponses.NAV_LEFT)

    async def cursor_right(self):
        await self._send_command(StormAudioCommands.NAV_RIGHT)
        await self._wait_for_response(StormAudioResponses.NAV_RIGHT)

    async def cursor_enter(self):
        await self._send_command(StormAudioCommands.NAV_OK)
        await self._wait_for_response(StormAudioResponses.NAV_OK)

    async def back(self):
        await self._send_command(StormAudioCommands.NAV_BACK)
        await self._wait_for_response(StormAudioResponses.NAV_BACK)

    # --- simple commands ---
    async def preset_next(self):
        await self._send_command(StormAudioCommands.PRESET_NEXT)

    async def preset_prev(self):
        await self._send_command(StormAudioCommands.PRESET_PREV)

    async def loudness_off(self):
        await self._send_command(StormAudioCommands.LOUDNESS_OFF)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_OFF)

    async def loudness_low(self):
        await self._send_command(StormAudioCommands.LOUDNESS_LOW)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_LOW)

    async def loudness_medium(self):
        await self._send_command(StormAudioCommands.LOUDNESS_MEDIUM)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_MEDIUM)

    async def loudness_full(self):
        await self._send_command(StormAudioCommands.LOUDNESS_FULL)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_FULL)

    async def bass_up(self):
        await self._send_command(StormAudioCommands.BASS_UP)

    async def bass_down(self):
        await self._send_command(StormAudioCommands.BASS_DOWN)

    async def bass_reset(self):
        await self._send_command(StormAudioCommands.BASS_RESET)

    async def treble_up(self):
        await self._send_command(StormAudioCommands.TREBLE_UP)

    async def treble_down(self):
        await self._send_command(StormAudioCommands.TREBLE_DOWN)

    async def treble_reset(self):
        await self._send_command(StormAudioCommands.TREBLE_RESET)

    async def brightness_up(self):
        await self._send_command(StormAudioCommands.BRIGHTNESS_UP)

    async def brightness_down(self):
        await self._send_command(StormAudioCommands.BRIGHTNESS_DOWN)

    async def brightness_reset(self):
        await self._send_command(StormAudioCommands.BRIGHTNESS_RESET)

    async def center_enhance_up(self):
        await self._send_command(StormAudioCommands.CENTER_ENHANCE_UP)

    async def center_enhance_down(self):
        await self._send_command(StormAudioCommands.CENTER_ENHANCE_DOWN)

    async def center_enhance_reset(self):
        await self._send_command(StormAudioCommands.CENTER_ENHANCE_RESET)

    async def surround_enhance_up(self):
        await self._send_command(StormAudioCommands.SURROUND_ENHANCE_UP)

    async def surround_enhance_down(self):
        await self._send_command(StormAudioCommands.SURROUND_ENHANCE_DOWN)

    async def surround_enhance_reset(self):
        await self._send_command(StormAudioCommands.SURROUND_ENHANCE_RESET)

    async def lfe_enhance_up(self):
        await self._send_command(StormAudioCommands.LFE_ENHANCE_UP)

    async def lfe_enhance_down(self):
        await self._send_command(StormAudioCommands.LFE_ENHANCE_DOWN)

    async def lfe_enhance_reset(self):
        await self._send_command(StormAudioCommands.LFE_ENHANCE_RESET)

    async def dolby_mode_off(self):
        await self._send_command(StormAudioCommands.DOLBY_MODE_OFF)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_OFF)

    async def dolby_mode_movie(self):
        await self._send_command(StormAudioCommands.DOLBY_MODE_MOVIE)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_MOVIE)

    async def dolby_mode_music(self):
        await self._send_command(StormAudioCommands.DOLBY_MODE_MUSIC)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_MUSIC)

    async def dolby_mode_night(self):
        await self._send_command(StormAudioCommands.DOLBY_MODE_NIGHT)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_NIGHT)
