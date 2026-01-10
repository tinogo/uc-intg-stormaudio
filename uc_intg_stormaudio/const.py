"""
Constants for the Integration.

This module contains constants used throughout the integration.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

from enum import StrEnum

from ucapi.media_player import States as MediaPlayerStates
from ucapi.remote import States as RemoteStates
from ucapi.sensor import States as SensorStates


class SimpleCommands(StrEnum):
    """
    Additional simple commands not covered by standard media-player features.

    Simple commands appear in the UI as buttons the user can press.
    """

    VOLUME_UP = "VOLUME_UP"
    VOLUME_DOWN = "VOLUME_DOWN"
    MUTE_ON = "MUTE_ON"
    MUTE_OFF = "MUTE_OFF"
    MUTE_TOGGLE = "MUTE_TOGGLE"
    CURSOR_UP = "CURSOR_UP"
    CURSOR_DOWN = "CURSOR_DOWN"
    CURSOR_LEFT = "CURSOR_LEFT"
    CURSOR_RIGHT = "CURSOR_RIGHT"
    CURSOR_ENTER = "CURSOR_ENTER"
    BACK = "BACK"
    PRESET_NEXT = "PRESET_NEXT"
    PRESET_PREV = "PRESET_PREV"
    LOUDNESS_OFF = "LOUDNESS_OFF"
    LOUDNESS_LOW = "LOUDNESS_LOW"
    LOUDNESS_MEDIUM = "LOUDNESS_MEDIUM"
    LOUDNESS_FULL = "LOUDNESS_FULL"
    BASS_UP = "BASS_UP"
    BASS_DOWN = "BASS_DOWN"
    BASS_RESET = "BASS_RESET"
    TREBLE_UP = "TREBLE_UP"
    TREBLE_DOWN = "TREBLE_DOWN"
    TREBLE_RESET = "TREBLE_RESET"
    BRIGHTNESS_UP = "BRIGHTNESS_UP"
    BRIGHTNESS_DOWN = "BRIGHTNESS_DOWN"
    BRIGHTNESS_RESET = "BRIGHTNESS_RESET"
    CENTER_ENHANCE_UP = "CENTER_ENHANCE_UP"
    CENTER_ENHANCE_DOWN = "CENTER_ENHANCE_DOWN"
    CENTER_ENHANCE_RESET = "CENTER_ENHANCE_RESET"
    SURROUND_ENHANCE_UP = "SURROUND_ENHANCE_UP"
    SURROUND_ENHANCE_DOWN = "SURROUND_ENHANCE_DOWN"
    SURROUND_ENHANCE_RESET = "SURROUND_ENHANCE_RESET"
    LFE_ENHANCE_UP = "LFE_ENHANCE_UP"
    LFE_ENHANCE_DOWN = "LFE_ENHANCE_DOWN"
    LFE_ENHANCE_RESET = "LFE_ENHANCE_RESET"
    DOLBY_OFF = "DOLBY_OFF"
    DOLBY_MOVIE = "DOLBY_MOVIE"
    DOLBY_MUSIC = "DOLBY_MUSIC"
    DOLBY_NIGHT = "DOLBY_NIGHT"
    STORM_XT_ON = "STORM_XT_ON"
    STORM_XT_OFF = "STORM_XT_OFF"
    STORM_XT_TOGGLE = "STORM_XT_TOGGLE"


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
    PRESET_X = "ssp.preset.[{}]"
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
    STORM_XT_ON = "ssp.stormxt.on"
    STORM_XT_OFF = "ssp.stormxt.off"
    STORM_XT_TOGGLE = "ssp.stormxt.toggle"


class StormAudioResponses(StrEnum):
    """Telnet responses from StormAudio device."""

    POWER_ON = "ssp.power.on"
    POWER_OFF = "ssp.power.off"
    PROC_STATE_OFF = "ssp.procstate.[0]"
    PROC_STATE_INDETERMINATE = "ssp.procstate.[1]"
    PROC_STATE_ON = "ssp.procstate.[2]"
    MUTE_ON = "ssp.mute.on"
    MUTE_OFF = "ssp.mute.off"
    VOLUME_X_FULL = "ssp.volume.[{}]"
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
    PRESET_LIST_START = "ssp.preset.start"
    PRESET_LIST_END = "ssp.preset.end"
    PRESET_LIST_X = "ssp.preset.list."
    PRESET_X_FULL = "ssp.preset.[{}]"
    PRESET_X = "ssp.preset."
    PRESET_CUSTOM_X = "ssp.preset.custom."
    INPUT_X_FULL = "ssp.input.[{}]"
    INPUT_X = "ssp.input."
    SURROUND_MODE_X = "ssp.surroundmode."
    DOLBY_MODE_OFF = "ssp.dolbymode.[0]"
    DOLBY_MODE_MOVIE = "ssp.dolbymode.[1]"
    DOLBY_MODE_MUSIC = "ssp.dolbymode.[2]"
    DOLBY_MODE_NIGHT = "ssp.dolbymode.[3]"
    STORM_XT_ON = "ssp.stormxt.on"
    STORM_XT_OFF = "ssp.stormxt.off"


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
    PRESET = "preset"
    STORM_XT = "storm_xt"
    UPMIXER_MODE = "upmixer"


class StormAudioStates(StrEnum):
    """Defines the possible states of the StormAudio device."""

    UNKNOWN = "UNKNOWN"
    UNAVAILABLE = "UNAVAILABLE"
    OFF = "OFF"
    ON = "ON"


MEDIA_PLAYER_STATE_MAPPING = {
    StormAudioStates.ON: MediaPlayerStates.ON,
    StormAudioStates.OFF: MediaPlayerStates.OFF,
    StormAudioStates.UNAVAILABLE: MediaPlayerStates.UNAVAILABLE,
    StormAudioStates.UNKNOWN: MediaPlayerStates.UNKNOWN,
}

REMOTE_STATE_MAPPING = {
    StormAudioStates.ON: RemoteStates.ON,
    StormAudioStates.OFF: RemoteStates.OFF,
    StormAudioStates.UNAVAILABLE: RemoteStates.UNAVAILABLE,
    StormAudioStates.UNKNOWN: RemoteStates.UNKNOWN,
}

SENSOR_STATE_MAPPING = {
    StormAudioStates.ON: SensorStates.ON,
    StormAudioStates.OFF: SensorStates.UNAVAILABLE,
    StormAudioStates.UNAVAILABLE: SensorStates.UNAVAILABLE,
    StormAudioStates.UNKNOWN: SensorStates.UNKNOWN,
}
