"""
Device Communication Module.

This module handles all communication with your device. It manages connections,
sends commands, and tracks the device state.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from asyncio import open_connection
from typing import Any

from ucapi_framework import PersistentConnectionDevice
from ucapi_framework.device import DeviceEvents

_LOG = logging.getLogger(__name__)

class StormAudioDevice(PersistentConnectionDevice):
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
        reader, writer = await open_connection(
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
            message = data.decode().strip()
            self.events.emit(
                DeviceEvents.UPDATE,
                self.identifier,
                {"message": message}
            )