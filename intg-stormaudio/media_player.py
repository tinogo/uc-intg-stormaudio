"""
Media Player Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any

import ucapi
from ucapi import MediaPlayer, media_player, EntityTypes
from ucapi.media_player import DeviceClasses, Attributes

import device
from const import StormAudioConfig, SimpleCommands
from ucapi_framework import create_entity_id

_LOG = logging.getLogger(__name__)

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

    def __init__(self, config_device: StormAudioConfig, device_instance: device.StormAudioDevice):
        """
        Initialize the media player entity.

        :param config_device: Device configuration from setup
        :param device_instance: The device instance to control
        """
        self._device = device_instance
        entity_id = create_entity_id(EntityTypes.MEDIA_PLAYER, config_device.identifier)

        _LOG.debug("Initializing media player entity: %s", entity_id)

        super().__init__(
            entity_id,
            config_device.name,
            FEATURES,
            attributes={
                Attributes.STATE: device_instance.state,
                Attributes.SOURCE_LIST: list(device_instance.source_list.keys()),
                Attributes.SOUND_MODE_LIST: list(device_instance.sound_mode_list.keys()),
                Attributes.VOLUME: device_instance.volume
            },
            device_class=DeviceClasses.RECEIVER,
            options={
                media_player.Options.SIMPLE_COMMANDS: [
                    member.value for member in SimpleCommands
                ]
            },
            cmd_handler=self.handle_command,
        )

    async def handle_command(
        self, entity: MediaPlayer, cmd_id: str, params: dict[str, Any] | None
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
        _LOG.info("Received command: %s %s", cmd_id, params if params else "")

        try:
            match cmd_id:
                case media_player.Commands.ON:
                    await self._device.power_on()

                case media_player.Commands.OFF:
                    await self._device.power_off()

                case media_player.Commands.TOGGLE:
                    await self._device.power_toggle()

                case media_player.Commands.VOLUME:
                    volume = params.get("volume") if params else None
                    await self._device.volume_x(volume)

                case media_player.Commands.VOLUME_UP:
                    await self._device.volume_up()

                case media_player.Commands.VOLUME_DOWN:
                    await self._device.volume_down()

                case media_player.Commands.MUTE:
                    await self._device.mute_on()

                case media_player.Commands.UNMUTE:
                    await self._device.mute_off()

                case media_player.Commands.MUTE_TOGGLE:
                    await self._device.mute_toggle()

                case media_player.Commands.SELECT_SOURCE:
                    source = params.get("source") if params else None
                    await self._device.select_source(source)

                case media_player.Commands.SELECT_SOUND_MODE:
                    mode = params.get("mode") if params else None
                    await self._device.select_sound_mode(mode)

                case media_player.Commands.CURSOR_UP:
                    await self._device.cursor_up()

                case media_player.Commands.CURSOR_DOWN:
                    await self._device.cursor_down()

                case media_player.Commands.CURSOR_LEFT:
                    await self._device.cursor_left()

                case media_player.Commands.CURSOR_RIGHT:
                    await self._device.cursor_right()

                case media_player.Commands.CURSOR_ENTER:
                    await self._device.cursor_enter()

                case media_player.Commands.BACK:
                    await self._device.back()

                case media_player.Commands.HOME:
                    await self._device.back()

                # --- Simple commands ---
                case SimpleCommands.PRESET_NEXT.value:
                    await self._device.preset_next()

                case SimpleCommands.PRESET_PREV.value:
                    await self._device.preset_prev()

                case SimpleCommands.LOUDNESS_OFF.value:
                    await self._device.loudness_off()

                case SimpleCommands.LOUDNESS_LOW.value:
                    await self._device.loudness_low()

                case SimpleCommands.LOUDNESS_MEDIUM.value:
                    await self._device.loudness_medium()

                case SimpleCommands.LOUDNESS_FULL.value:
                    await self._device.loudness_full()

                case SimpleCommands.BASS_UP.value:
                    await self._device.bass_up()

                case SimpleCommands.BASS_DOWN.value:
                    await self._device.bass_down()

                case SimpleCommands.BASS_RESET.value:
                    await self._device.bass_reset()

                case SimpleCommands.TREBLE_UP.value:
                    await self._device.treble_up()

                case SimpleCommands.TREBLE_DOWN.value:
                    await self._device.treble_down()

                case SimpleCommands.TREBLE_RESET.value:
                    await self._device.treble_reset()

                case SimpleCommands.BRIGHTNESS_UP.value:
                    await self._device.brightness_up()

                case SimpleCommands.BRIGHTNESS_DOWN.value:
                    await self._device.brightness_down()

                case SimpleCommands.BRIGHTNESS_RESET.value:
                    await self._device.brightness_reset()

                # --- unhandled commands ---
                case _:
                    _LOG.warning("Unhandled command: %s", cmd_id)
                    return ucapi.StatusCodes.NOT_IMPLEMENTED

            return ucapi.StatusCodes.OK

        except Exception as ex:
            _LOG.error("Error executing command %s: %s", cmd_id, ex)
            return ucapi.StatusCodes.BAD_REQUEST
