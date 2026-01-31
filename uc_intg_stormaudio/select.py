"""
Select Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any, Literal

from ucapi import EntityTypes, Select, StatusCodes
from ucapi.select import Commands as SelectCommands
from ucapi_framework import Entity, create_entity_id

from uc_intg_stormaudio.const import Loggers, SelectType
from uc_intg_stormaudio.device import StormAudioDevice

_LOG = logging.getLogger(Loggers.SELECT)

_selects = {
    SelectType.AURO_PRESET: "Auro-Matic Preset",
    SelectType.AURO_STRENGTH: "Auro-Matic Strength",
    SelectType.PRESET: "Preset",
    SelectType.SOUND_MODE: "Sound mode",
}


class StormAudioSelect(Select, Entity):
    """Select for the StormAudio ISPs."""

    def __init__(
        self,
        device: StormAudioDevice,
        select_type: SelectType,
    ):
        """Initialize the select entity."""
        self._device = device
        self._select_type = select_type

        select_config = self._get_select_config(select_type, device)

        _LOG.debug("Initializing select: %s", select_config["identifier"])

        super().__init__(
            identifier=select_config["identifier"],
            name=select_config["name"],
            attributes=select_config["attributes"],
            cmd_handler=self.handle_command,
        )

    def _get_select_config(
        self, select_type: SelectType, device: StormAudioDevice
    ) -> dict[str, Any]:
        """Get select configuration based on type."""
        select = {}
        select_entity_id = create_entity_id(
            EntityTypes.SELECT,
            device.identifier,
            select_type,
        )

        match select_type:
            case select_type if _selects.get(select_type) is not None:
                select = {
                    "identifier": select_entity_id,
                    "name": f"{device.name} Select: {_selects.get(select_type)}",
                    "attributes": self._device.get_device_attributes(select_entity_id),
                }

            case _:
                raise ValueError(f"Unsupported select type: {select_type}")
        return select

    async def handle_command(
        self,
        entity: Select,
        cmd_id: str,
        params: dict[str, Any] | None,
        _: Any | None = None,
    ) -> StatusCodes:
        """Handle select commands from the remote."""
        _LOG.debug(
            "[%s] Received command for select entity: %s %s",
            entity.id,
            cmd_id,
            params if params else "",
        )

        match self._select_type:
            case SelectType.AURO_PRESET:
                return await self._handle_auro_preset_command(cmd_id, params)

            case SelectType.AURO_STRENGTH:
                return await self._handle_auro_strength_command(cmd_id, params)

            case SelectType.PRESET:
                return await self._handle_preset_command(cmd_id, params)

            case SelectType.SOUND_MODE:
                return await self._handle_sound_mode_command(cmd_id, params)

    async def _handle_auro_preset_command(
        self, cmd_id: str, params: dict[str, Any] | None
    ) -> Literal[StatusCodes.OK]:
        auro_preset_list = self._device.device_attributes.auro_preset_list
        match cmd_id:
            case SelectCommands.SELECT_OPTION:
                await self._device.auro_preset_x(params["option"])

            case SelectCommands.SELECT_FIRST:
                first_auro_preset_name = auro_preset_list[0]
                await self._device.auro_preset_x(first_auro_preset_name)

            case SelectCommands.SELECT_LAST:
                last_auro_preset_name = auro_preset_list[-1]
                await self._device.auro_preset_x(last_auro_preset_name)

            case SelectCommands.SELECT_NEXT:
                current_index = auro_preset_list.index(
                    self._device.device_attributes.auro_preset
                )
                if current_index < len(auro_preset_list) - 1:
                    next_auro_preset_name = auro_preset_list[current_index + 1]
                    await self._device.auro_preset_x(next_auro_preset_name)
                elif params["cycle"]:
                    next_auro_preset_name = auro_preset_list[0]
                    await self._device.auro_preset_x(next_auro_preset_name)

            case SelectCommands.SELECT_PREVIOUS:
                current_index = auro_preset_list.index(
                    self._device.device_attributes.auro_preset
                )
                if current_index > 0:
                    previous_auro_preset_name = auro_preset_list[current_index - 1]
                    await self._device.auro_preset_x(previous_auro_preset_name)
                elif params["cycle"]:
                    previous_auro_preset_name = auro_preset_list[len(auro_preset_list)]
                    await self._device.auro_preset_x(previous_auro_preset_name)

        return StatusCodes.OK

    async def _handle_auro_strength_command(
        self, cmd_id: str, params: dict[str, Any] | None
    ) -> Literal[StatusCodes.OK]:
        match cmd_id:
            case SelectCommands.SELECT_OPTION:
                await self._device.auro_strength_x(params["option"])

            case SelectCommands.SELECT_FIRST:
                await self._device.auro_strength_x(
                    self._device.device_attributes.auro_strength_list[0]
                )

            case SelectCommands.SELECT_LAST:
                await self._device.auro_strength_x(
                    self._device.device_attributes.auro_strength_list[-1]
                )

            case SelectCommands.SELECT_NEXT:
                next_value = self._device.device_attributes.auro_strength + 1

                if next_value in self._device.device_attributes.auro_strength_list:
                    await self._device.auro_strength_x(next_value)
                elif params["cycle"]:
                    await self._device.auro_strength_x(0)

            case SelectCommands.SELECT_PREVIOUS:
                previous_value = self._device.device_attributes.auro_strength - 1

                if previous_value in self._device.device_attributes.auro_strength_list:
                    await self._device.auro_strength_x(previous_value)
                elif params["cycle"]:
                    await self._device.auro_strength_x(
                        self._device.device_attributes.auro_strength_list[-1]
                    )

        return StatusCodes.OK

    async def _handle_sound_mode_command(
        self, cmd_id: str, params: dict[str, Any] | None
    ) -> Literal[StatusCodes.OK]:
        sound_mode_list = self._device.device_attributes.sound_mode_list
        match cmd_id:
            case SelectCommands.SELECT_OPTION:
                await self._device.select_sound_mode(params["option"])

            case SelectCommands.SELECT_FIRST:
                first_sound_mode_name = sound_mode_list[0]
                await self._device.select_sound_mode(first_sound_mode_name)

            case SelectCommands.SELECT_LAST:
                last_sound_mode_name = sound_mode_list[-1]
                await self._device.select_sound_mode(last_sound_mode_name)

            case SelectCommands.SELECT_NEXT:
                current_index = sound_mode_list.index(
                    self._device.device_attributes.sound_mode
                )
                if current_index < len(sound_mode_list) - 1:
                    next_sound_mode_name = sound_mode_list[current_index + 1]
                    await self._device.select_sound_mode(next_sound_mode_name)
                elif params["cycle"]:
                    next_sound_mode_name = sound_mode_list[0]
                    await self._device.select_sound_mode(next_sound_mode_name)

            case SelectCommands.SELECT_PREVIOUS:
                current_index = sound_mode_list.index(
                    self._device.device_attributes.sound_mode
                )
                if current_index > 0:
                    previous_sound_mode_name = sound_mode_list[current_index - 1]
                    await self._device.select_sound_mode(previous_sound_mode_name)
                elif params["cycle"]:
                    previous_sound_mode_name = sound_mode_list[len(sound_mode_list)]
                    await self._device.select_sound_mode(previous_sound_mode_name)

        return StatusCodes.OK

    async def _handle_preset_command(
        self, cmd_id: str, params: dict[str, Any] | None
    ) -> Literal[StatusCodes.OK]:
        match cmd_id:
            case SelectCommands.SELECT_OPTION:
                await self._device.preset_x(params["option"])

            case SelectCommands.SELECT_FIRST:
                first_preset_name = self._device.device_attributes.preset_list[0]
                await self._device.preset_x(first_preset_name)

            case SelectCommands.SELECT_LAST:
                last_preset_name = self._device.device_attributes.preset_list[-1]
                await self._device.preset_x(last_preset_name)

            case SelectCommands.SELECT_NEXT:
                await self._device.preset_next()

            case SelectCommands.SELECT_PREVIOUS:
                await self._device.preset_prev()

        return StatusCodes.OK
