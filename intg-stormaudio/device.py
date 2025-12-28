"""
Device Communication Module.

This module handles all communication with your device. It manages connections,
sends commands, and tracks the device state.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import asyncio
import logging
import telnetlib3
from typing import Any

from ucapi import EntityTypes
from ucapi.media_player import States, Attributes as MediaAttr
from ucapi_framework import PersistentConnectionDevice, create_entity_id
from ucapi_framework.device import DeviceEvents

from const import StormAudioCommands, StormAudioResponses

_LOG = logging.getLogger(__name__)


class StormAudioDevice(PersistentConnectionDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._waiters: list[tuple[str, asyncio.Future[str]]] = []
        self._state = States.UNKNOWN

    @property
    def state(self) -> States:
        """Return the current device state."""
        return self._state

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

            if message == StormAudioResponses.PROC_STATE_OFF:
                self._update_state(States.OFF)
            elif message == StormAudioResponses.PROC_STATE_INITIALISING:
                # Maps both initializing and shutting down to OFF
                # as they are not "fully booted"
                self._update_state(States.OFF)
            elif message == StormAudioResponses.PROC_STATE_ON:
                self._update_state(States.ON)
            else:
                self.events.emit(
                    DeviceEvents.UPDATE,
                    create_entity_id(EntityTypes.MEDIA_PLAYER, self.identifier),
                    {"message": message}
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
            create_entity_id(EntityTypes.MEDIA_PLAYER, self.identifier),
            {MediaAttr.STATE: self._state}
        )

    async def power_on(self):
        """Power on the StormAudio processor."""
        await self._send_command(StormAudioCommands.POWER_ON)
        await self._wait_for_response(StormAudioResponses.POWER_ON)

    async def power_off(self):
        """Power off the StormAudio processor."""
        await self._send_command(StormAudioCommands.POWER_OFF)
        await self._wait_for_response(StormAudioResponses.POWER_OFF)

    async def power_toggle(self):
        """Toggle power of the StormAudio processor."""
        # Create futures for both possible responses
        on_future = asyncio.get_running_loop().create_future()
        off_future = asyncio.get_running_loop().create_future()
        
        # Add waiters BEFORE sending command to avoid race conditions
        self._waiters.append((StormAudioResponses.POWER_ON, on_future))
        self._waiters.append((StormAudioResponses.POWER_OFF, off_future))

        try:
            await self._send_command(StormAudioCommands.POWER_TOGGLE)
            
            done, pending = await asyncio.wait(
                [on_future, off_future],
                return_when=asyncio.FIRST_COMPLETED,
                timeout=5.0
            )
            
            # Cleanup pending waiters
            for p in pending:
                p.cancel()
                for pattern, fut in self._waiters[:]:
                    if fut == p:
                        self._waiters.remove((pattern, fut))

            if not done:
                _LOG.warning("[%s] Timeout waiting for power toggle response", self.log_id)
                # Cleanup the ones that timed out
                for pattern, fut in self._waiters[:]:
                    if fut in [on_future, off_future]:
                        self._waiters.remove((pattern, fut))
                return

            await done.pop()
        except Exception:
            # Emergency cleanup of waiters if something fails before wait
            for pattern, fut in self._waiters[:]:
                if fut in [on_future, off_future]:
                    self._waiters.remove((pattern, fut))
            raise