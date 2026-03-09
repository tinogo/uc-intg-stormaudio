# pylint: disable=duplicate-code

"""
Media Player Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any, Callable

from ucapi import EntityTypes, MediaPlayer, StatusCodes, media_player
from ucapi.media_player import Attributes as MediaAttr
from ucapi.media_player import DeviceClasses, States
from ucapi_framework import Entity, create_entity_id

from uc_intg_stormaudio.config import StormAudioConfig
from uc_intg_stormaudio.const import (
    MEDIA_PLAYER_STATE_MAPPING,
    Loggers,
    SimpleCommands,
    StormAudioStates,
)
from uc_intg_stormaudio.device import StormAudioDevice
from uc_intg_stormaudio.simple_commands import get_simple_command_map

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


class StormAudioMediaPlayer(MediaPlayer, Entity):
    """
    Media Player entity for your device.

    This class handles all media player commands and maintains the entity state.
    """

    def __init__(self, device_config: StormAudioConfig, device: StormAudioDevice):
        """
        Initialize the media player entity.

        :param device_config: Device configuration from the setup
        :param device: The device instance to control
        """
        self._device = device

        self._command_map: dict[str, Callable] = {
            media_player.Commands.ON.value: device.power_on,
            media_player.Commands.OFF.value: device.power_off,
            media_player.Commands.TOGGLE.value: device.power_toggle,
            media_player.Commands.VOLUME_UP.value: device.volume_up,
            media_player.Commands.VOLUME_DOWN.value: device.volume_down,
            media_player.Commands.MUTE.value: device.mute_on,
            media_player.Commands.UNMUTE.value: device.mute_off,
            media_player.Commands.MUTE_TOGGLE.value: device.mute_toggle,
            media_player.Commands.CURSOR_UP.value: device.cursor_up,
            media_player.Commands.CURSOR_DOWN.value: device.cursor_down,
            media_player.Commands.CURSOR_LEFT.value: device.cursor_left,
            media_player.Commands.CURSOR_RIGHT.value: device.cursor_right,
            media_player.Commands.CURSOR_ENTER.value: device.cursor_enter,
            media_player.Commands.BACK.value: device.back,
            media_player.Commands.HOME.value: device.back,
            **get_simple_command_map(self._device),
        }

        entity_id = create_entity_id(EntityTypes.MEDIA_PLAYER, device.identifier)

        _LOG.debug("Initializing media player entity: %s", entity_id)

        super().__init__(
            identifier=entity_id,
            name=f"{device_config.name} Media Player",
            features=FEATURES,
            attributes=device.get_device_attributes(entity_id),
            device_class=DeviceClasses.RECEIVER,
            options={
                media_player.Options.SIMPLE_COMMANDS: [
                    member.value for member in SimpleCommands
                ]
            },
            cmd_handler=self.handle_command,
        )

        self.subscribe_to_device(device)

    async def handle_command(
        self,
        entity: MediaPlayer,
        cmd_id: str,
        params: dict[str, Any] | None,
        _: Any | None = None,
    ) -> StatusCodes:
        """
        Handle media player commands from the remote.

        This method is called by the integration API when a command is sent
        to this media player entity.

        :param entity: The media player entity receiving the command
        :param cmd_id: The command identifier
        :param params: Optional command parameters
        :param _: Optional parameter containing the websocket resource

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
                    return StatusCodes.NOT_IMPLEMENTED

            return StatusCodes.OK

        except Exception as ex:  # pylint: disable=broad-exception-caught
            _LOG.error("Error executing command %s: %s", cmd_id, ex)
            return StatusCodes.BAD_REQUEST

    def map_entity_states(self, device_state: StormAudioStates) -> States:
        """Convert a device-specific state to a UC API entity state."""
        return MEDIA_PLAYER_STATE_MAPPING[device_state]

    async def sync_state(self) -> None:
        """Update the media player attributes."""
        audio_stream = self._device.device_attributes.audio_stream
        audio_format = self._device.device_attributes.audio_format
        audio_sample_rate = self._device.device_attributes.audio_sample_rate

        self.update(
            {
                MediaAttr.STATE: MEDIA_PLAYER_STATE_MAPPING[self._device.state],
                MediaAttr.MEDIA_TITLE: f"Audio: {audio_stream}, {audio_format}, {audio_sample_rate}"
                if self._device.device_attributes.audio_stream != "None"
                else None,
                MediaAttr.SOURCE: self._device.device_attributes.source,
                MediaAttr.SOURCE_LIST: self._device.device_attributes.source_list,
                MediaAttr.SOUND_MODE: self._device.device_attributes.actual_sound_mode,
                MediaAttr.SOUND_MODE_LIST: self._device.device_attributes.sound_mode_list,
                MediaAttr.VOLUME: self._device.device_attributes.volume,
                MediaAttr.MUTED: self._device.device_attributes.muted,
            }
        )
