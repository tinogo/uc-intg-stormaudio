# pylint: disable=duplicate-code

"""
Remote Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import asyncio
import logging
from typing import Any

import ucapi
from ucapi import EntityTypes, Remote, remote
from ucapi_framework import create_entity_id, Entity

from uc_intg_stormaudio.config import StormAudioConfig
from uc_intg_stormaudio.const import Loggers, SimpleCommands
from uc_intg_stormaudio.device import StormAudioDevice

_LOG = logging.getLogger(Loggers.REMOTE)

FEATURES = [
    remote.Features.ON_OFF,
    remote.Features.SEND_CMD,
    remote.Features.TOGGLE,
]

_PRESET_CMD_PREFIX = "PRESET_"
_SOURCE_CMD_PREFIX = "SOURCE_"
_VOLUME_CMD_PREFIX = "VOLUME_"


class StormAudioRemote(Remote, Entity):
    """
    Remote entity for your device.

    This class handles all Remote commands and maintains the entity state.
    """

    def __init__(
        self, device_config: StormAudioConfig, device: StormAudioDevice
    ):
        """
        Initialize the remote entity.

        :param device_config: Device configuration from the setup
        :param device: The device instance to control
        """
        self._command_map = {
            remote.Commands.ON.value: device.power_on,
            remote.Commands.OFF.value: device.power_off,
            remote.Commands.TOGGLE.value: device.power_toggle,
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
        }

        entity_id = create_entity_id(EntityTypes.REMOTE, device.identifier)

        _LOG.debug("Initializing remote entity: %s", entity_id)

        Remote.__init__(
            self,
            identifier=entity_id,
            name=f"{device_config.name} Remote",
            features=FEATURES,
            attributes=device.get_device_attributes(entity_id),
            simple_commands=[member.value for member in SimpleCommands],
            cmd_handler=self.handle_command,
        )

        self._device = device

    async def handle_command(
        self,
        entity: Remote,
        cmd_id: str,
        params: dict[str, Any] | None,
        _: Any | None = None,
    ) -> ucapi.StatusCodes:
        """
        Handle commands from the remote.

        This method is called by the integration API when a command is sent
        to this remote entity.

        :param entity: The remote receiving the command
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

                case remote.Commands.SEND_CMD:
                    if params:
                        command = params.get("command", None)
                        repeat = params.get("repeat", 1)
                        delay = params.get("delay", 100)
                        await self._handle_send_cmd(command, repeat, delay)
                    else:
                        raise ValueError(
                            "Cannot process command without any given parameters."
                        )

                case remote.Commands.SEND_CMD_SEQUENCE:
                    if params:
                        command_list = params.get("sequence") if params else None
                        repeat = params.get("repeat", 1)
                        delay = params.get("delay", 100)

                        for command in command_list:
                            await self._handle_send_cmd(command, repeat, delay)
                    else:
                        raise ValueError(
                            "Cannot process command without any given parameters."
                        )

                # --- unhandled commands ---
                case _:
                    _LOG.warning("Unhandled command: %s", cmd_id)
                    return ucapi.StatusCodes.NOT_IMPLEMENTED

            return ucapi.StatusCodes.OK

        except Exception as ex:  # pylint: disable=broad-exception-caught
            _LOG.error("Error executing command %s: %s", cmd_id, ex)
            return ucapi.StatusCodes.BAD_REQUEST

    async def _handle_send_cmd(self, command: str, repeat: int, delay: int) -> None:
        for _ in range(repeat):
            if command in self._command_map:
                await self._command_map[command]()
            elif isinstance(command, str) and command.startswith(_PRESET_CMD_PREFIX):
                preset_name = command[len(_PRESET_CMD_PREFIX) :]  # noqa: E203
                await self._device.preset_x(preset_name)
            elif isinstance(command, str) and command.startswith(_SOURCE_CMD_PREFIX):
                source_name = command[len(_SOURCE_CMD_PREFIX) :]  # noqa: E203
                await self._device.select_source(source_name)
            elif isinstance(command, str) and command.startswith(_VOLUME_CMD_PREFIX):
                volume = int(command[len(_VOLUME_CMD_PREFIX) :])  # noqa: E203
                await self._device.volume_x(volume)
            else:
                await self._device.custom_command(command)

            if delay > 0:
                await asyncio.sleep(delay / 1000)
