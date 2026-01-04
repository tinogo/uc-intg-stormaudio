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
    """TCP-Client for interacting with the StormAudio device."""

    def __init__(self, address: str, port: int):
        """Initialize the client."""
        self._waiters: list[tuple[str, asyncio.Future[str]]] = []
        self._address = address
        self._port = port

    @property
    def log_id(self) -> str:
        """Return a log identifier for debugging."""
        return f"{self._address}:{self._port}"

    async def connect(self) -> tuple[StreamReader, StreamWriter]:
        """Establish a TCP connection to the device."""
        reader, writer = await asyncio.open_connection(self._address, self._port)

        return reader, writer

    async def close(self, connection: tuple[StreamReader, StreamWriter]) -> None:
        """Close the TCP connection."""
        _reader, writer = connection
        writer.close()
        await writer.wait_closed()

    async def send_command(
        self, connection: tuple[StreamReader, StreamWriter], command: str
    ) -> None:
        """Send a command to the device."""
        _reader, writer = connection
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
        self, connection: tuple[StreamReader, StreamWriter], message_handler=None
    ) -> None:
        """Retrieve and process the response messages from the TCP connection."""
        reader, _writer = connection

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
