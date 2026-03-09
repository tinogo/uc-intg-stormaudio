"""
This module provides a map of simple commands to their corresponding methods in the device.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

from typing import Callable

from uc_intg_stormaudio.const import (
    SimpleCommands,
)
from uc_intg_stormaudio.device import StormAudioDevice


def get_simple_command_map(device: StormAudioDevice) -> dict[str, Callable]:
    """Return a map of simple commands to their corresponding methods in the device."""
    return {
        SimpleCommands.VOLUME_UP.value: device.volume_up,
        SimpleCommands.VOLUME_DOWN.value: device.volume_down,
        SimpleCommands.MUTE_ON.value: device.mute_on,
        SimpleCommands.MUTE_OFF.value: device.mute_off,
        SimpleCommands.MUTE_TOGGLE.value: device.mute_toggle,
        SimpleCommands.CURSOR_UP.value: device.cursor_up,
        SimpleCommands.CURSOR_DOWN.value: device.cursor_down,
        SimpleCommands.CURSOR_LEFT.value: device.cursor_left,
        SimpleCommands.CURSOR_RIGHT.value: device.cursor_right,
        SimpleCommands.CURSOR_ENTER.value: device.cursor_enter,
        SimpleCommands.BACK.value: device.back,
        SimpleCommands.PRESET_NEXT.value: device.preset_next,
        SimpleCommands.PRESET_PREV.value: device.preset_prev,
        SimpleCommands.LOUDNESS_OFF.value: device.loudness_off,
        SimpleCommands.LOUDNESS_LOW.value: device.loudness_low,
        SimpleCommands.LOUDNESS_MEDIUM.value: device.loudness_medium,
        SimpleCommands.LOUDNESS_FULL.value: device.loudness_full,
        SimpleCommands.BASS_UP.value: device.bass_up,
        SimpleCommands.BASS_DOWN.value: device.bass_down,
        SimpleCommands.BASS_RESET.value: device.bass_reset,
        SimpleCommands.TREBLE_UP.value: device.treble_up,
        SimpleCommands.TREBLE_DOWN.value: device.treble_down,
        SimpleCommands.TREBLE_RESET.value: device.treble_reset,
        SimpleCommands.BRIGHTNESS_UP.value: device.brightness_up,
        SimpleCommands.BRIGHTNESS_DOWN.value: device.brightness_down,
        SimpleCommands.BRIGHTNESS_RESET.value: device.brightness_reset,
        SimpleCommands.CENTER_ENHANCE_UP.value: device.center_enhance_up,
        SimpleCommands.CENTER_ENHANCE_DOWN.value: device.center_enhance_down,
        SimpleCommands.CENTER_ENHANCE_RESET.value: device.center_enhance_reset,
        SimpleCommands.SURROUND_ENHANCE_UP.value: device.surround_enhance_up,
        SimpleCommands.SURROUND_ENHANCE_DOWN.value: device.surround_enhance_down,
        SimpleCommands.SURROUND_ENHANCE_RESET.value: device.surround_enhance_reset,
        SimpleCommands.LFE_ENHANCE_UP.value: device.lfe_enhance_up,
        SimpleCommands.LFE_ENHANCE_DOWN.value: device.lfe_enhance_down,
        SimpleCommands.LFE_ENHANCE_RESET.value: device.lfe_enhance_reset,
        SimpleCommands.DOLBY_OFF.value: device.dolby_mode_off,
        SimpleCommands.DOLBY_MOVIE.value: device.dolby_mode_movie,
        SimpleCommands.DOLBY_MUSIC.value: device.dolby_mode_music,
        SimpleCommands.DOLBY_NIGHT.value: device.dolby_mode_night,
        SimpleCommands.STORM_XT_ON.value: device.storm_xt_on,
        SimpleCommands.STORM_XT_OFF.value: device.storm_xt_off,
        SimpleCommands.STORM_XT_TOGGLE.value: device.storm_xt_toggle,
        SimpleCommands.AURO_PRESET_SMALL.value: device.auro_preset_small,
        SimpleCommands.AURO_PRESET_MEDIUM.value: device.auro_preset_medium,
        SimpleCommands.AURO_PRESET_LARGE.value: device.auro_preset_large,
        SimpleCommands.AURO_PRESET_SPEECH.value: device.auro_preset_speech,
        SimpleCommands.DOLBY_CENTER_SPREAD_ON.value: device.dolby_center_spread_on,
        SimpleCommands.DOLBY_CENTER_SPREAD_OFF.value: device.dolby_center_spread_off,
        SimpleCommands.DOLBY_CENTER_SPREAD_TOGGLE.value: device.dolby_center_spread_toggle,
        SimpleCommands.DOLBY_VIRTUALIZER_ON.value: device.dolby_virtualizer_on,
        SimpleCommands.DOLBY_VIRTUALIZER_OFF.value: device.dolby_virtualizer_off,
        SimpleCommands.DOLBY_VIRTUALIZER_TOGGLE.value: device.dolby_virtualizer_toggle,
    }
