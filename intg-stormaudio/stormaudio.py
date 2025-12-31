"""
Client Module.

This module handles the TCP/Telnet connection to the StormAudio device.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import asyncio
import logging
from asyncio import StreamReader, StreamWriter

from const import Loggers

_LOG = logging.getLogger(Loggers.DEVICE)


class StormAudioClient:
    def __init__(self, address: str, port: int):
        self._waiters: list[tuple[str, asyncio.Future[str]]] = []
        self._address = address
        self._port = port

    @property
    def log_id(self) -> str:
        """Return a log identifier for debugging."""
        return f"{self._address}:{self._port}"

    async def connect(self) -> dict[str, StreamReader | StreamWriter]:
        reader, writer = await asyncio.open_connection(self._address, self._port)

        return {"reader": reader, "writer": writer}

    async def close(self, connection: dict[str, StreamReader | StreamWriter]) -> None:
        connection["writer"].close()
        await connection["writer"].wait_closed()

    async def send_command(
        self, connection: dict[str, StreamReader | StreamWriter], command: str
    ) -> None:
        """Send a command to the device."""

        writer: StreamWriter = connection["writer"]
        _LOG.debug("[%s] Sending: %s", self.log_id, command)
        writer.write((command + "\n").encode())
        await writer.drain()

    async def wait_for_response(self, pattern: str, timeout: float = 5.0) -> str | None:
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

    def _notify_waiters(self, message: str) -> None:
        for pattern, future in self._waiters[:]:
            if pattern in message and not future.done():
                future.set_result(message)
                self._waiters.remove((pattern, future))

    async def parse_response_messages(
        self, connection: dict[str, StreamReader | StreamWriter], message_handler=None
    ) -> None:
        reader = connection["reader"]

        while True:
            data = await reader.readline()
            if not data:
                break  # Connection closed

            # Process message
            message = data.decode().strip()
            _LOG.debug("[%s] Received: %s", self.log_id, message)

            self._notify_waiters(message)

            if message_handler:
                message_handler(message)
