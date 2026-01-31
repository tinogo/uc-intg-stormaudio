"""
Select Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any

from ucapi import EntityTypes, Select, StatusCodes
from ucapi.select import Commands as SelectCommands
from ucapi_framework import Entity, create_entity_id

from uc_intg_stormaudio.const import Loggers, SelectType
from uc_intg_stormaudio.device import StormAudioDevice

_LOG = logging.getLogger(Loggers.SELECT)

_selects = {
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

        self._device = device

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

    async def handle_command(  # pylint: disable=too-many-branches
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

        if self._select_type == SelectType.PRESET:
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

        if self._select_type == SelectType.SOUND_MODE:
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

        return StatusCodes.NOT_IMPLEMENTED
