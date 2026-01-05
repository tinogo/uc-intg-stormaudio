"""
Device Communication Module.

This module handles all communication with your device. It manages connections,
sends commands, and tracks the device state.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import json
import logging
from typing import Any

from const import Loggers, StormAudioCommands, StormAudioResponses
from stormaudio import StormAudioClient
from ucapi import EntityTypes
from ucapi.media_player import Attributes as MediaAttr
from ucapi.media_player import States
from ucapi_framework import PersistentConnectionDevice, create_entity_id
from ucapi_framework.device import DeviceEvents

_LOG = logging.getLogger(Loggers.DEVICE)

MIN_VOLUME = 0
MAX_VOLUME = 100
MAX_TIME_OUT = 20


class StormAudioDevice(PersistentConnectionDevice):
    """StormAudio Device."""

    def __init__(self, *args, **kwargs):
        """Initialize the device."""
        super().__init__(*args, **kwargs)

        self._state = States.UNKNOWN
        self._sources: dict[str, int] = {}
        self._surround_modes: dict[str, int] = {
            "Native": 0,
            "Stereo Downmix": 1,
            "Dolby Surround": 2,
            "DTS Neural:X": 3,
            "Auro-Matic": 4,
        }
        self._volume: int = 40
        self._muted: bool = False
        self._client = StormAudioClient(self.address, self.device_config.port)

    @property
    def state(self) -> States:
        """Return the current device state."""
        return self._state

    @property
    def source_list(self) -> list[str]:
        """Returns a list of the available input sources."""
        return list(self._sources.keys())

    @property
    def volume(self) -> int:
        """Returns the current device volume."""
        return self._volume

    @property
    def muted(self) -> bool:
        """Returns whether the device is currently muted or not."""
        return self._muted

    @property
    def sound_mode_list(self) -> list[str]:
        """Returns a list of the available sound modes."""
        return list(self._surround_modes.keys())

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

    async def connect(self) -> bool:
        """Establish persistent connection with reconnection logic."""
        if self._reconnect_task:
            await self.disconnect()

        return await super().connect()

    async def establish_connection(self) -> Any:
        """Establish connection to the device."""
        return await self._client.connect()

    async def close_connection(self) -> None:
        """Close the connection."""
        if self._connection:
            await self._client.close(self._connection)

    async def maintain_connection(self) -> None:
        """Maintain the connection."""

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
                    self._muted = message == StormAudioResponses.MUTE_ON
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.VOLUME_X):
                    # The UC remotes currently only support relative volume scales.
                    # That's why we need to convert the absolute values from the ISPs.
                    self._volume = (
                        int(float(message[len(StormAudioResponses.VOLUME_X) : -1]))  # noqa: E203
                        + MAX_VOLUME
                    )
                    self._update_attributes()

                case StormAudioResponses.INPUT_LIST_START:
                    self._sources = {}

                case message if message.startswith(StormAudioResponses.INPUT_LIST_X):
                    input_name, input_id, *_tail = json.loads(
                        message[len(StormAudioResponses.INPUT_LIST_X) :]  # noqa: E203
                    )

                    self._sources.update({input_name: input_id})

                case StormAudioResponses.INPUT_LIST_END:
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
        return await self._client.wait_for_response(pattern, timeout)

    def _update_attributes(self) -> None:
        """Update the device attributes via an event."""
        self.events.emit(
            DeviceEvents.UPDATE,
            self.entity_id,
            {
                MediaAttr.STATE: self._state,
                MediaAttr.SOURCE_LIST: self.source_list,
                MediaAttr.SOUND_MODE_LIST: self.sound_mode_list,
                MediaAttr.VOLUME: self.volume,
                MediaAttr.MUTED: self.muted,
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
        """Set the volume of the StormAudio processor."""
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
            StormAudioCommands.INPUT_X.format(self._sources.get(source))
        )
        await self._wait_for_response(
            StormAudioResponses.INPUT_X.format(self._sources.get(source))
        )

    async def select_sound_mode(self, mode):
        """Set the surround mode of the StormAudio processor."""
        await self._send_command(
            StormAudioCommands.SURROUND_MODE_X.format(self._surround_modes.get(mode))
        )

    async def cursor_up(self):
        """Navigate up."""
        await self._send_command(StormAudioCommands.NAV_UP)
        await self._wait_for_response(StormAudioResponses.NAV_UP)

    async def cursor_down(self):
        """Navigate down."""
        await self._send_command(StormAudioCommands.NAV_DOWN)
        await self._wait_for_response(StormAudioResponses.NAV_DOWN)

    async def cursor_left(self):
        """Navigate left."""
        await self._send_command(StormAudioCommands.NAV_LEFT)
        await self._wait_for_response(StormAudioResponses.NAV_LEFT)

    async def cursor_right(self):
        """Navigate right."""
        await self._send_command(StormAudioCommands.NAV_RIGHT)
        await self._wait_for_response(StormAudioResponses.NAV_RIGHT)

    async def cursor_enter(self):
        """Enter the selected item."""
        await self._send_command(StormAudioCommands.NAV_OK)
        await self._wait_for_response(StormAudioResponses.NAV_OK)

    async def back(self):
        """Navigate back."""
        await self._send_command(StormAudioCommands.NAV_BACK)
        await self._wait_for_response(StormAudioResponses.NAV_BACK)

    # --- simple commands ---
    async def preset_next(self):
        """Set the next preset."""
        await self._send_command(StormAudioCommands.PRESET_NEXT)

    async def preset_prev(self):
        """Set the previous preset."""
        await self._send_command(StormAudioCommands.PRESET_PREV)

    async def loudness_off(self):
        """Set the loudness to off."""
        await self._send_command(StormAudioCommands.LOUDNESS_OFF)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_OFF)

    async def loudness_low(self):
        """Set the loudness to low."""
        await self._send_command(StormAudioCommands.LOUDNESS_LOW)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_LOW)

    async def loudness_medium(self):
        """Set the loudness to medium."""
        await self._send_command(StormAudioCommands.LOUDNESS_MEDIUM)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_MEDIUM)

    async def loudness_full(self):
        """Set the loudness to full."""
        await self._send_command(StormAudioCommands.LOUDNESS_FULL)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_FULL)

    async def bass_up(self):
        """Increase the bass by 1dB."""
        await self._send_command(StormAudioCommands.BASS_UP)

    async def bass_down(self):
        """Decrease the bass by 1dB."""
        await self._send_command(StormAudioCommands.BASS_DOWN)

    async def bass_reset(self):
        """Reset the bass."""
        await self._send_command(StormAudioCommands.BASS_RESET)

    async def treble_up(self):
        """Increase the treble by 1dB."""
        await self._send_command(StormAudioCommands.TREBLE_UP)

    async def treble_down(self):
        """Decrease the treble by 1dB."""
        await self._send_command(StormAudioCommands.TREBLE_DOWN)

    async def treble_reset(self):
        """Reset the treble."""
        await self._send_command(StormAudioCommands.TREBLE_RESET)

    async def brightness_up(self):
        """Increase the brightness by 1dB."""
        await self._send_command(StormAudioCommands.BRIGHTNESS_UP)

    async def brightness_down(self):
        """Decrease the brightness by 1dB."""
        await self._send_command(StormAudioCommands.BRIGHTNESS_DOWN)

    async def brightness_reset(self):
        """Reset the brightness."""
        await self._send_command(StormAudioCommands.BRIGHTNESS_RESET)

    async def center_enhance_up(self):
        """Increase the center enhancement by 1dB."""
        await self._send_command(StormAudioCommands.CENTER_ENHANCE_UP)

    async def center_enhance_down(self):
        """Decrease the center enhancement by 1dB."""
        await self._send_command(StormAudioCommands.CENTER_ENHANCE_DOWN)

    async def center_enhance_reset(self):
        """Reset the center enhancement."""
        await self._send_command(StormAudioCommands.CENTER_ENHANCE_RESET)

    async def surround_enhance_up(self):
        """Increase the surround enhancement by 1dB."""
        await self._send_command(StormAudioCommands.SURROUND_ENHANCE_UP)

    async def surround_enhance_down(self):
        """Decrease the surround enhancement by 1dB."""
        await self._send_command(StormAudioCommands.SURROUND_ENHANCE_DOWN)

    async def surround_enhance_reset(self):
        """Reset the surround enhancement."""
        await self._send_command(StormAudioCommands.SURROUND_ENHANCE_RESET)

    async def lfe_enhance_up(self):
        """Increase the LFE enhancement by 1dB."""
        await self._send_command(StormAudioCommands.LFE_ENHANCE_UP)

    async def lfe_enhance_down(self):
        """Decrease the LFE enhancement by 1dB."""
        await self._send_command(StormAudioCommands.LFE_ENHANCE_DOWN)

    async def lfe_enhance_reset(self):
        """Reset the LFE enhancement."""
        await self._send_command(StormAudioCommands.LFE_ENHANCE_RESET)

    async def dolby_mode_off(self):
        """Set the Dolby mode to off mode."""
        await self._send_command(StormAudioCommands.DOLBY_MODE_OFF)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_OFF)

    async def dolby_mode_movie(self):
        """Set the Dolby mode to movie mode."""
        await self._send_command(StormAudioCommands.DOLBY_MODE_MOVIE)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_MOVIE)

    async def dolby_mode_music(self):
        """Set the Dolby mode to music mode."""
        await self._send_command(StormAudioCommands.DOLBY_MODE_MUSIC)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_MUSIC)

    async def dolby_mode_night(self):
        """Set the Dolby mode to night mode."""
        await self._send_command(StormAudioCommands.DOLBY_MODE_NIGHT)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_NIGHT)
