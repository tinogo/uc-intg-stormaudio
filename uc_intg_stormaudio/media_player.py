# pylint: disable=duplicate-code

"""
Media Player Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any

import ucapi
from ucapi import EntityTypes, MediaPlayer, media_player
from ucapi.media_player import DeviceClasses
from ucapi_framework import create_entity_id

from uc_intg_stormaudio.config import StormAudioConfig
from uc_intg_stormaudio.const import Loggers, SimpleCommands
from uc_intg_stormaudio.device import StormAudioDevice

_LOG = logging.getLogger(Loggers.MEDIA_PLAYER)

FEATURES = [
    media_player.Features.ON_OFF,
    media_player.Features.DPAD,
    media_player.Features.TOGGLE,
    media_player.Features.VOLUME,
    media_player.Features.VOLUME_UP_DOWN,
    media_player.Features.HOME,
    media_player.Features.MUTE,
    media_player.Features.UNMUTE,
    media_player.Features.MUTE_TOGGLE,
    media_player.Features.SELECT_SOUND_MODE,
    media_player.Features.SELECT_SOURCE,
]


class StormAudioMediaPlayer(MediaPlayer):
    """
    Media Player entity for your device.

    This class handles all media player commands and maintains the entity state.
    """

    def __init__(
        self, config_device: StormAudioConfig, device_instance: StormAudioDevice
    ):
        """
        Initialize the media player entity.

        :param config_device: Device configuration from the setup
        :param device_instance: The device instance to control
        """
        self._device = device_instance
        self._command_map = {
            media_player.Commands.ON.value: self._device.power_on,
            media_player.Commands.OFF.value: self._device.power_off,
            media_player.Commands.TOGGLE.value: self._device.power_toggle,
            media_player.Commands.VOLUME_UP.value: self._device.volume_up,
            media_player.Commands.VOLUME_DOWN.value: self._device.volume_down,
            media_player.Commands.MUTE.value: self._device.mute_on,
            media_player.Commands.UNMUTE.value: self._device.mute_off,
            media_player.Commands.MUTE_TOGGLE.value: self._device.mute_toggle,
            media_player.Commands.CURSOR_UP.value: self._device.cursor_up,
            media_player.Commands.CURSOR_DOWN.value: self._device.cursor_down,
            media_player.Commands.CURSOR_LEFT.value: self._device.cursor_left,
            media_player.Commands.CURSOR_RIGHT.value: self._device.cursor_right,
            media_player.Commands.CURSOR_ENTER.value: self._device.cursor_enter,
            media_player.Commands.BACK.value: self._device.back,
            media_player.Commands.HOME.value: self._device.back,
            SimpleCommands.VOLUME_UP.value: self._device.volume_up,
            SimpleCommands.VOLUME_DOWN.value: self._device.volume_down,
            SimpleCommands.MUTE_ON.value: self._device.mute_on,
            SimpleCommands.MUTE_OFF.value: self._device.mute_off,
            SimpleCommands.MUTE_TOGGLE.value: self._device.mute_toggle,
            SimpleCommands.CURSOR_UP.value: self._device.cursor_up,
            SimpleCommands.CURSOR_DOWN.value: self._device.cursor_down,
            SimpleCommands.CURSOR_LEFT.value: self._device.cursor_left,
            SimpleCommands.CURSOR_RIGHT.value: self._device.cursor_right,
            SimpleCommands.CURSOR_ENTER.value: self._device.cursor_enter,
            SimpleCommands.BACK.value: self._device.back,
            SimpleCommands.PRESET_NEXT.value: self._device.preset_next,
            SimpleCommands.PRESET_PREV.value: self._device.preset_prev,
            SimpleCommands.LOUDNESS_OFF.value: self._device.loudness_off,
            SimpleCommands.LOUDNESS_LOW.value: self._device.loudness_low,
            SimpleCommands.LOUDNESS_MEDIUM.value: self._device.loudness_medium,
            SimpleCommands.LOUDNESS_FULL.value: self._device.loudness_full,
            SimpleCommands.BASS_UP.value: self._device.bass_up,
            SimpleCommands.BASS_DOWN.value: self._device.bass_down,
            SimpleCommands.BASS_RESET.value: self._device.bass_reset,
            SimpleCommands.TREBLE_UP.value: self._device.treble_up,
            SimpleCommands.TREBLE_DOWN.value: self._device.treble_down,
            SimpleCommands.TREBLE_RESET.value: self._device.treble_reset,
            SimpleCommands.BRIGHTNESS_UP.value: self._device.brightness_up,
            SimpleCommands.BRIGHTNESS_DOWN.value: self._device.brightness_down,
            SimpleCommands.BRIGHTNESS_RESET.value: self._device.brightness_reset,
            SimpleCommands.CENTER_ENHANCE_UP.value: self._device.center_enhance_up,
            SimpleCommands.CENTER_ENHANCE_DOWN.value: self._device.center_enhance_down,
            SimpleCommands.CENTER_ENHANCE_RESET.value: self._device.center_enhance_reset,
            SimpleCommands.SURROUND_ENHANCE_UP.value: self._device.surround_enhance_up,
            SimpleCommands.SURROUND_ENHANCE_DOWN.value: self._device.surround_enhance_down,
            SimpleCommands.SURROUND_ENHANCE_RESET.value: self._device.surround_enhance_reset,
            SimpleCommands.LFE_ENHANCE_UP.value: self._device.lfe_enhance_up,
            SimpleCommands.LFE_ENHANCE_DOWN.value: self._device.lfe_enhance_down,
            SimpleCommands.LFE_ENHANCE_RESET.value: self._device.lfe_enhance_reset,
            SimpleCommands.DOLBY_OFF.value: self._device.dolby_mode_off,
            SimpleCommands.DOLBY_MOVIE.value: self._device.dolby_mode_movie,
            SimpleCommands.DOLBY_MUSIC.value: self._device.dolby_mode_music,
            SimpleCommands.DOLBY_NIGHT.value: self._device.dolby_mode_night,
            SimpleCommands.STORM_XT_ON.value: self._device.storm_xt_on,
            SimpleCommands.STORM_XT_OFF.value: self._device.storm_xt_off,
            SimpleCommands.STORM_XT_TOGGLE.value: self._device.storm_xt_toggle,
        }

        entity_id = create_entity_id(
            EntityTypes.MEDIA_PLAYER, device_instance.identifier
        )

        _LOG.debug("Initializing media player entity: %s", entity_id)

        super().__init__(
            identifier=entity_id,
            name=config_device.name,
            features=FEATURES,
            attributes=device_instance.get_device_attributes(entity_id),
            device_class=DeviceClasses.RECEIVER,
            options={
                media_player.Options.SIMPLE_COMMANDS: [
                    member.value for member in SimpleCommands
                ]
            },
            cmd_handler=self.handle_command,
        )

    async def handle_command(
        self,
        entity: MediaPlayer,
        cmd_id: str,
        params: dict[str, Any] | None,
    ) -> ucapi.StatusCodes:
        """
        Handle media player commands from the remote.

        This method is called by the integration API when a command is sent
        to this media player entity.

        :param entity: The media player entity receiving the command
        :param cmd_id: The command identifier
        :param params: Optional command parameters

        :return: Status code indicating success or failure
        """
        _LOG.info(
            "[%s] Received command: %s %s", entity.id, cmd_id, params if params else ""
        )

        try:
            match cmd_id:
                case cmd_id if cmd_id in self._command_map:
                    await self._command_map[cmd_id]()

                # complex commands (with parameters)
                case media_player.Commands.VOLUME:
                    volume = params.get("volume") if params else None
                    await self._device.volume_x(volume)

                case media_player.Commands.SELECT_SOURCE:
                    source = params.get("source") if params else None
                    await self._device.select_source(source)

                case media_player.Commands.SELECT_SOUND_MODE:
                    mode = params.get("mode") if params else None
                    await self._device.select_sound_mode(mode)

                # --- unhandled commands ---
                case _:
                    _LOG.warning("Unhandled command: %s", cmd_id)
                    return ucapi.StatusCodes.NOT_IMPLEMENTED

            return ucapi.StatusCodes.OK

        except Exception as ex:  # pylint: disable=broad-exception-caught
            _LOG.error("Error executing command %s: %s", cmd_id, ex)
            return ucapi.StatusCodes.BAD_REQUEST
