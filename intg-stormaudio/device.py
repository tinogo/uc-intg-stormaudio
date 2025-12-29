"""
Device Communication Module.

This module handles all communication with your device. It manages connections,
sends commands, and tracks the device state.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import asyncio
import logging
import telnetlib3
import json
from typing import Any, Dict

from ucapi import EntityTypes
from ucapi.media_player import States, Attributes as MediaAttr
from ucapi_framework import PersistentConnectionDevice, create_entity_id
from ucapi_framework.device import DeviceEvents

from const import StormAudioCommands, StormAudioResponses

_LOG = logging.getLogger(__name__)

_min_volume = 0
_max_volume = 100

class StormAudioDevice(PersistentConnectionDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._waiters: list[tuple[str, asyncio.Future[str]]] = []
        self._state = States.UNKNOWN
        self._source_list = self._device_config.input_list
        self._sound_mode_list = {"Native": 0, "Stereo Downmix": 1, "Dolby Surround": 2, 'DTS Neural:X': 3, 'Auro-Matic': 4}
        self._entity_id = create_entity_id(EntityTypes.MEDIA_PLAYER, self.identifier)

    @property
    def state(self) -> States:
        """Return the current device state."""
        return self._state

    @property
    def source_list(self) -> Dict[str, int]:
        """Returns a dictionary of available input sources."""
        return self._source_list

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

    async def establish_connection(self) -> Any:
        reader, writer = await telnetlib3.open_connection(
            self.address, self._device_config.port
        )

        return {"reader": reader, "writer": writer}

    async def close_connection(self) -> None:
        if self._connection:
            self._connection["writer"].close()
            await self._connection["writer"].wait_closed()

    async def maintain_connection(self) -> None:
        reader = self._connection["reader"]

        while True:
            data = await reader.readline()
            if not data:
                break  # Connection closed

            # Process message
            message = data.strip()
            _LOG.debug("[%s] Received: %s", self.log_id, message)

            # Notify waiters
            for pattern, future in self._waiters[:]:
                if pattern in message and not future.done():
                    future.set_result(message)
                    self._waiters.remove((pattern, future))

            match message:
                case StormAudioResponses.PROC_STATE_ON:
                    self._update_state(States.ON)
                case StormAudioResponses.PROC_STATE_OFF | StormAudioResponses.PROC_STATE_INDETERMINATE:
                    # Maps both the initialization and the process of shutting down to OFF
                    # as they are not "fully booted"
                    self._update_state(States.OFF)
                case StormAudioResponses.MUTE_ON:
                    self.events.emit(
                        DeviceEvents.UPDATE,
                        self._entity_id,
                        {MediaAttr.MUTED: True}
                    )
                case StormAudioResponses.MUTE_OFF:
                    self.events.emit(
                        DeviceEvents.UPDATE,
                        self._entity_id,
                        {MediaAttr.MUTED: False}
                    )
                case message if message.startswith(StormAudioResponses.VOLUME_X):
                    # The UC remotes currently only support relative volume scales.
                    # That's why we need to convert the absolute values from the ISPs.
                    volume = int(float(message[len(StormAudioResponses.VOLUME_X):-1])) + _max_volume

                    self.events.emit(
                        DeviceEvents.UPDATE,
                        self._entity_id,
                        {MediaAttr.VOLUME: volume}
                    )
                case message if message.startswith(StormAudioResponses.INPUT_LIST_X):
                    input_name, input_id, *tail = json.loads(message[len(StormAudioResponses.INPUT_LIST_X):])

                    if input_name not in self._source_list:
                        self._source_list.update({input_name: input_id})

                        self.events.emit(
                            DeviceEvents.UPDATE,
                            self._entity_id,
                            {MediaAttr.SOURCE_LIST: list(self.source_list.keys())}
                        )

    async def _send_command(self, command: str) -> None:
        """Send a command to the device."""
        if not self._connection:
            _LOG.error("[%s] Cannot send command, not connected", self.log_id)
            return

        writer = self._connection["writer"]
        _LOG.debug("[%s] Sending: %s", self.log_id, command)
        writer.write(command + "\n")
        await writer.drain()

    async def _wait_for_response(self, pattern: str, timeout: float = 5.0) -> str | None:
        """Wait for a specific response from the device."""
        future = asyncio.get_running_loop().create_future()
        self._waiters.append((pattern, future))

        try:
            return await asyncio.wait_for(future, timeout=timeout)
        except asyncio.TimeoutError:
            _LOG.warning("[%s] Timeout waiting for response: %s", self.log_id, pattern)
            if (pattern, future) in self._waiters:
                self._waiters.remove((pattern, future))
            return None

    def _update_state(self, state: States) -> None:
        """Update device state and emit event."""
        self._state = state
        self.events.emit(
            DeviceEvents.UPDATE,
            self._entity_id,
            {MediaAttr.STATE: self._state}
        )

    async def power_on(self):
        """Power on the StormAudio processor."""
        await self._send_command(StormAudioCommands.POWER_ON)

    async def power_off(self):
        """Power off the StormAudio processor."""
        await self._send_command(StormAudioCommands.POWER_OFF)

    async def power_toggle(self):
        """Toggle power of the StormAudio processor."""
        await self._send_command(StormAudioCommands.POWER_TOGGLE)

    async def mute_on(self):
        """Mute the StormAudio processor."""
        await self._send_command(StormAudioCommands.MUTE_ON)

    async def mute_off(self):
        """Unmute the StormAudio processor."""
        await self._send_command(StormAudioCommands.MUTE_OFF)

    async def mute_toggle(self):
        """Toggle mute of the StormAudio processor."""
        await self._send_command(StormAudioCommands.MUTE_TOGGLE)

    async def volume(self, volume):
        # The UC remotes only support relative volume scales for now.
        # That's why we need to convert the absolute values from the ISPs.
        sanitized_volume = max(_min_volume, min(_max_volume, int(volume))) - _max_volume
        await self._send_command(StormAudioCommands.VOLUME_X.format(sanitized_volume))

    async def volume_up(self):
        """Increase the volume of the StormAudio processor by 1dB."""
        await self._send_command(StormAudioCommands.VOLUME_UP)

    async def volume_down(self):
        """Decrease the volume of the StormAudio processor by 1dB."""
        await self._send_command(StormAudioCommands.VOLUME_DOWN)

    async def select_source(self, source):
        """Decrease the volume of the StormAudio processor by 1dB."""
        await self._send_command(StormAudioCommands.INPUT_X.format(self.source_list.get(source)))

    async def select_sound_mode(self, mode):
        """Set the surround mode of the StormAudio processor."""
        await self._send_command(StormAudioCommands.SURROUND_MODE_X.format(self.sound_mode_list.get(mode)))

    async def cursor_up(self):
        await self._send_command(StormAudioCommands.NAV_UP)

    async def cursor_down(self):
        await self._send_command(StormAudioCommands.NAV_DOWN)

    async def cursor_left(self):
        await self._send_command(StormAudioCommands.NAV_LEFT)

    async def cursor_right(self):
        await self._send_command(StormAudioCommands.NAV_RIGHT)

    async def cursor_enter(self):
        await self._send_command(StormAudioCommands.NAV_OK)

    async def back(self):
        await self._send_command(StormAudioCommands.NAV_BACK)

    # --- simple commands ---
    async def preset_next(self):
        await self._send_command(StormAudioCommands.PRESET_NEXT)

    async def preset_prev(self):
        await self._send_command(StormAudioCommands.PRESET_PREV)

    async def loudness_off(self):
        await self._send_command(StormAudioCommands.LOUDNESS_OFF)

    async def loudness_low(self):
        await self._send_command(StormAudioCommands.LOUDNESS_LOW)

    async def loudness_medium(self):
        await self._send_command(StormAudioCommands.LOUDNESS_MEDIUM)

    async def loudness_full(self):
        await self._send_command(StormAudioCommands.LOUDNESS_FULL)

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
