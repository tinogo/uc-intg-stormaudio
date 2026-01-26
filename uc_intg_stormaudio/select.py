import logging
from enum import Enum
from typing import Any

from ucapi import Entity as UcEntity
from ucapi import StatusCodes
from ucapi_framework import Entity, create_entity_id

from uc_intg_stormaudio import Loggers, StormAudioConfig, StormAudioDevice

_LOG = logging.getLogger(Loggers.SELECT)


class EntityTypes(str, Enum):
    SELECT = "select"


class StormAudioSelect(UcEntity, Entity):
    def __init__(self, device_config: StormAudioConfig, device: StormAudioDevice):
        entity_id = create_entity_id("select", device.identifier)

        _LOG.debug("Initializing media player entity: %s", entity_id)

        super().__init__(
            identifier=entity_id,
            entity_type=EntityTypes.SELECT,
            name=f"{device_config.name} Select",
            features=[],
            attributes=device.get_device_attributes(entity_id),
            cmd_handler=self.handle_command,
        )

        self._device = device

    async def handle_command(
        self,
        entity: UcEntity,
        cmd_id: str,
        params: dict[str, Any] | None,
        _: Any | None = None,
    ) -> StatusCodes:
        _LOG.debug(
            "[%s] Received command for select entity: %s %s",
            entity.id,
            cmd_id,
            params if params else "",
        )

        return StatusCodes.OK
