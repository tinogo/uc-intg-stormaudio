"""
Configuration for the Integration.

This module contains the configuration dataclass

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

from dataclasses import dataclass, field


@dataclass
class StormAudioConfig:
    """
    Device configuration dataclass.

    This dataclass holds all the configuration needed to connect to and
    identify a device.
    """

    identifier: str
    """Unique identifier of the device (e.g., MAC address, serial number)."""

    name: str
    """Friendly name of the device for display purposes."""

    address: str
    """IP address or hostname of the device."""

    port: int = 23
    """Port number for device communication."""

    sources: dict[str, int] = field(default_factory=dict)
    """Dictionary containing all the currently configured sources/inputs of the StormAudio ISP."""

    presets: dict[str, int] = field(default_factory=dict)
    """Dictionary containing all the currently configured presets of the StormAudio ISP."""
