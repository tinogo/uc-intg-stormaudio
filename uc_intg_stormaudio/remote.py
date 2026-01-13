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
from ucapi_framework import create_entity_id

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
_VOLUME_CMD_PREFIX = "VOLUME_"


class StormAudioRemote(Remote):
    """
    Remote entity for your device.

    This class handles all Remote commands and maintains the entity state.
    """

    def __init__(
        self, config_device: StormAudioConfig, device_instance: StormAudioDevice
    ):
        """
        Initialize the remote entity.

        :param config_device: Device configuration from the setup
        :param device_instance: The device instance to control
        """
        self._device = device_instance
        self._command_map = {
            remote.Commands.ON.value: self._device.power_on,
            remote.Commands.OFF.value: self._device.power_off,
            remote.Commands.TOGGLE.value: self._device.power_toggle,
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

        entity_id = create_entity_id(EntityTypes.REMOTE, device_instance.identifier)

        _LOG.debug("Initializing remote entity: %s", entity_id)

        super().__init__(
            identifier=entity_id,
            name=config_device.name,
            features=FEATURES,
            attributes=device_instance.get_device_attributes(entity_id),
            simple_commands=[member.value for member in SimpleCommands],
            cmd_handler=self.handle_command,
        )

    async def handle_command(
        self,
        entity: Remote,
        cmd_id: str,
        params: dict[str, Any] | None,
    ) -> ucapi.StatusCodes:
        """
        Handle commands from the remote.

        This method is called by the integration API when a command is sent
        to this remote entity.

        :param entity: The remote receiving the command
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
            elif isinstance(command, str) and command.startswith(_VOLUME_CMD_PREFIX):
                volume = int(command[len(_VOLUME_CMD_PREFIX) :])  # noqa: E203
                await self._device.volume_x(volume)
            else:
                await self._device.custom_command(command)

            if delay > 0:
                await asyncio.sleep(delay / 1000)
