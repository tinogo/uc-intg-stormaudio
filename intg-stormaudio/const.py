"""
Constants for the Integration.

This module contains configuration dataclasses and constants used throughout
the integration. Customize these for your specific device.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Dict


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

    input_list: Dict[str, int] = field(default_factory=dict)
    """List of inputs for the device, if available."""


class SimpleCommands(StrEnum):
    """
    Additional simple commands not covered by standard media-player features.

    Simple commands appear in the UI as buttons the user can press.
    Add commands specific to your device here.
    """

    PRESET_NEXT = "Preset: next"
    PRESET_PREV = "Preset: previous"
    LOUDNESS_OFF = "Loudness: off"
    LOUDNESS_LOW = "Loudness: low"
    LOUDNESS_MEDIUM = "Loudness: medium"
    LOUDNESS_FULL = "Loudness: full"
    BASS_UP = "Bass: +1dB"
    BASS_DOWN = "Bass: -1dB"
    BASS_RESET = "Bass: 0dB"
    TREBLE_UP = "Treble: +1dB"
    TREBLE_DOWN = "Treble: -1dB"
    TREBLE_RESET = "Treble: 0dB"
    BRIGHTNESS_UP = "Brightness: +1dB"
    BRIGHTNESS_DOWN = "Brightness: -1dB"
    BRIGHTNESS_RESET = "Brightness: 0dB"


class StormAudioCommands(StrEnum):
    """Telnet commands for StormAudio device."""

    CLOSE = "ssp.close"
    POWER_ON = "ssp.power.on"
    POWER_OFF = "ssp.power.off"
    POWER_TOGGLE = "ssp.power.toggle"
    PROC_STATE = "ssp.procstate"
    MUTE_ON = "ssp.mute.on"
    MUTE_OFF = "ssp.mute.off"
    MUTE_TOGGLE = "ssp.mute.toggle"
    VOLUME_X = "ssp.vol.[{}]"
    VOLUME_DOWN = "ssp.vol.down"
    VOLUME_UP = "ssp.vol.up"
    INPUT_X = "ssp.input.[{}]"
    SURROUND_MODE_X = "ssp.surroundmode.[{}]"
    PRESET_NEXT = "ssp.preset.next"
    PRESET_PREV = "ssp.preset.prev"
    LOUDNESS_OFF = "ssp.loudness.[0]"
    LOUDNESS_LOW = "ssp.loudness.[1]"
    LOUDNESS_MEDIUM = "ssp.loudness.[2]"
    LOUDNESS_FULL = "ssp.loudness.[3]"
    BASS_UP = "ssp.bass.up"
    BASS_DOWN = "ssp.bass.down"
    BASS_RESET = "ssp.bass.[0]"
    TREBLE_UP = "ssp.treble.up"
    TREBLE_DOWN = "ssp.treble.down"
    TREBLE_RESET = "ssp.treble.[0]"
    BRIGHTNESS_UP = "ssp.brightness.up"
    BRIGHTNESS_DOWN = "ssp.brightness.down"
    BRIGHTNESS_RESET = "ssp.brightness.[0]"


class StormAudioResponses(StrEnum):
    """Telnet responses from StormAudio device."""

    CLOSE = 'ssp.close'
    POWER_ON = "ssp.power.on"
    POWER_OFF = "ssp.power.off"
    PROC_STATE_OFF = "ssp.procstate.[0]"
    PROC_STATE_INDETERMINATE = "ssp.procstate.[1]"
    PROC_STATE_ON = "ssp.procstate.[2]"
    MUTE_ON = "ssp.mute.on"
    MUTE_OFF = "ssp.mute.off"
    VOLUME_X = 'ssp.vol.['
    INPUT_LIST_X = 'ssp.input.list.'
    SURROUND_MODE_X = 'ssp.surroundmode.'
