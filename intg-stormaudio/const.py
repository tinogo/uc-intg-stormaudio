"""
Constants for the Integration.

This module contains configuration dataclasses and constants used throughout
the integration. Customize these for your specific device.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

from dataclasses import dataclass
from enum import StrEnum


@dataclass
class StormAudioConfig:
    """
    Device configuration dataclass.

    This dataclass holds all the configuration needed to connect to and
    identify a device. Add or remove fields as needed for your device.
    """

    identifier: str
    """Unique identifier of the device (e.g., MAC address, serial number)."""

    name: str
    """Friendly name of the device for display purposes."""

    address: str
    """IP address or hostname of the device."""

    port: int = 23
    """Port number for device communication."""

    # TODO: Add any additional configuration fields your device needs
    # Examples:
    # model: str = ""
    # """Device model for feature detection."""


class SimpleCommands(StrEnum):
    """
    Additional simple commands not covered by standard media-player features.

    Simple commands appear in the UI as buttons the user can press.
    Add commands specific to your device here.

    Example:
        PRESET_1 = "Preset 1"
        PRESET_2 = "Preset 2"
        NIGHT_MODE = "Night Mode"
    """

    # TODO: Define simple commands for your device
    # EXAMPLE_COMMAND = "Example Command"
    pass
