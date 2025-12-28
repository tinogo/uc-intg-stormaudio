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

from ucapi.media_player import States
from ucapi_framework import PersistentConnectionDevice
from ucapi_framework.device import DeviceEvents

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

            self.events.emit(
                DeviceEvents.UPDATE,
                self.identifier,
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

    async def power_on(self):
        """Power on the StormAudio processor."""
        await self._send_command("ssp.power.on")
        response = await self._wait_for_response("ssp.power.on")

        if response == "ssp.power.on":
            await self._send_command("ssp.procstate")
            state_resp = await self._wait_for_response("ssp.procstate")

            if state_resp:
                if state_resp == "ssp.procstate.0":
                    self._state = States.STANDBY
                elif state_resp == "ssp.procstate.1":
                    self._state = States.STANDBY
                elif state_resp == "ssp.procstate.2":
                    self._state = States.ON

                self.events.emit(
                    DeviceEvents.UPDATE,
                    self.identifier,
                    {"state": self._state}
                )

    async def power_off(self):
        """Power off the StormAudio processor."""
        await self._send_command("ssp.power.off")
        response = await self._wait_for_response("ssp.power.off")

        if response == "ssp.power.off":
            await self._send_command("ssp.procstate")
            state_resp = await self._wait_for_response("ssp.procstate")

            if state_resp:
                if state_resp == "ssp.procstate.0":
                    self._state = States.STANDBY
                elif state_resp == "ssp.procstate.1":
                    self._state = States.STANDBY
                elif state_resp == "ssp.procstate.2":
                    self._state = States.ON

                self.events.emit(
                    DeviceEvents.UPDATE,
                    self.identifier,
                    {"state": self._state}
                )