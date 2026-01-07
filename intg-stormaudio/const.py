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
    CENTER_ENHANCE_UP = "Center-Enhance: +1dB"
    CENTER_ENHANCE_DOWN = "Center-Enhance: -1dB"
    CENTER_ENHANCE_RESET = "Center-Enhance: 0dB"
    SURROUND_ENHANCE_UP = "Surround-Enhance: +1dB"
    SURROUND_ENHANCE_DOWN = "Surround-Enhance: -1dB"
    SURROUND_ENHANCE_RESET = "Surround-Enhance: 0dB"
    LFE_ENHANCE_UP = "LFE-Enhance: +1dB"
    LFE_ENHANCE_DOWN = "LFE-Enhance: -1dB"
    LFE_ENHANCE_RESET = "LFE-Enhance: 0dB"
    DOLBY_MODE_OFF = "Dolby mode: off"
    DOLBY_MODE_MOVIE = "Dolby mode: Movie"
    DOLBY_MODE_MUSIC = "Dolby mode: Music"
    DOLBY_MODE_NIGHT = "Dolby mode: Night"


class StormAudioCommands(StrEnum):
    """Telnet commands for StormAudio device."""

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
    NAV_UP = "ssp.nav.up"
    NAV_DOWN = "ssp.nav.down"
    NAV_LEFT = "ssp.nav.left"
    NAV_RIGHT = "ssp.nav.right"
    NAV_OK = "ssp.nav.ok"
    NAV_BACK = "ssp.nav.back"
    BASS_UP = "ssp.bass.up"
    BASS_DOWN = "ssp.bass.down"
    BASS_RESET = "ssp.bass.[0]"
    TREBLE_UP = "ssp.treble.up"
    TREBLE_DOWN = "ssp.treble.down"
    TREBLE_RESET = "ssp.treble.[0]"
    BRIGHTNESS_UP = "ssp.brightness.up"
    BRIGHTNESS_DOWN = "ssp.brightness.down"
    BRIGHTNESS_RESET = "ssp.brightness.[0]"
    CENTER_ENHANCE_UP = "ssp.c_en.up"
    CENTER_ENHANCE_DOWN = "ssp.c_en.down"
    CENTER_ENHANCE_RESET = "ssp.c_en.[0]"
    SURROUND_ENHANCE_UP = "ssp.s_en.up"
    SURROUND_ENHANCE_DOWN = "ssp.s_en.down"
    SURROUND_ENHANCE_RESET = "ssp.s_en.[0]"
    LFE_ENHANCE_UP = "ssp.lfe_en.up"
    LFE_ENHANCE_DOWN = "ssp.lfe_en.down"
    LFE_ENHANCE_RESET = "ssp.lfe_en.[0]"
    DOLBY_MODE_OFF = "ssp.dolbymode.[0]"
    DOLBY_MODE_MOVIE = "ssp.dolbymode.[1]"
    DOLBY_MODE_MUSIC = "ssp.dolbymode.[2]"
    DOLBY_MODE_NIGHT = "ssp.dolbymode.[3]"


class StormAudioResponses(StrEnum):
    """Telnet responses from StormAudio device."""

    POWER_ON = "ssp.power.on"
    POWER_OFF = "ssp.power.off"
    PROC_STATE_OFF = "ssp.procstate.[0]"
    PROC_STATE_INDETERMINATE = "ssp.procstate.[1]"
    PROC_STATE_ON = "ssp.procstate.[2]"
    MUTE_ON = "ssp.mute.on"
    MUTE_OFF = "ssp.mute.off"
    VOLUME_X = "ssp.vol.["
    LOUDNESS_OFF = "ssp.loudness.[0]"
    LOUDNESS_LOW = "ssp.loudness.[1]"
    LOUDNESS_MEDIUM = "ssp.loudness.[2]"
    LOUDNESS_FULL = "ssp.loudness.[3]"
    NAV_UP = "ssp.nav.up"
    NAV_DOWN = "ssp.nav.down"
    NAV_LEFT = "ssp.nav.left"
    NAV_RIGHT = "ssp.nav.right"
    NAV_OK = "ssp.nav.ok"
    NAV_BACK = "ssp.nav.back"
    INPUT_LIST_START = "ssp.input.start"
    INPUT_LIST_END = "ssp.input.end"
    INPUT_LIST_X = "ssp.input.list."
    INPUT_X = "ssp.input.[{}]"
    SURROUND_MODE_X = "ssp.surroundmode."
    DOLBY_MODE_OFF = "ssp.dolbymode.[0]"
    DOLBY_MODE_MOVIE = "ssp.dolbymode.[1]"
    DOLBY_MODE_MUSIC = "ssp.dolbymode.[2]"
    DOLBY_MODE_NIGHT = "ssp.dolbymode.[3]"
    ZONE_PROFILES_END = "ssp.zones.profiles.end"


class Loggers(StrEnum):
    """Defines the various logger types."""

    DRIVER = "driver"
    MEDIA_PLAYER = "media_player"
    DEVICE = "device"
    SENSOR = "sensor"
    SETUP_FLOW = "setup_flow"


class SensorType(StrEnum):
    """Defines the supported sensor types for StormAudio devices."""

    VOLUME_DB = "volume_db"
    MUTE = "mute"
