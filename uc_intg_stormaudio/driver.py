"""
StormAudio Integration Driver for Remote Two/3.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

from ucapi_framework import BaseIntegrationDriver

from uc_intg_stormaudio.config import StormAudioConfig
from uc_intg_stormaudio.device import StormAudioDevice
from uc_intg_stormaudio.media_player import StormAudioMediaPlayer
from uc_intg_stormaudio.remote import StormAudioRemote
from uc_intg_stormaudio.sensor import StormAudioSensor, create_sensors


class StormAudioIntegrationDriver(
    BaseIntegrationDriver[StormAudioDevice, StormAudioConfig]
):
    """StormAudio Integration Driver."""

    async def async_register_available_entities(
        self, device_config: StormAudioConfig, device: StormAudioDevice
    ) -> None:
        """Register available entities for a device (async version)."""
        entities: list[StormAudioMediaPlayer | StormAudioRemote | StormAudioSensor] = [
            StormAudioMediaPlayer(device_config, device),
            StormAudioRemote(device_config, device),
            *create_sensors(device),
        ]

        for entity in entities:
            if self.api.available_entities.contains(entity.id):
                self.api.available_entities.remove(entity.id)
            self.api.available_entities.add(entity)
