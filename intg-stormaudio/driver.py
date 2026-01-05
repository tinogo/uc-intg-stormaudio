"""
Remote Two/3 Integration Driver.

This is the main entry point for the integration driver. It initializes
the driver, sets up logging, and starts the integration API.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import asyncio
import logging
import os

from const import Loggers, StormAudioConfig
from device import StormAudioDevice
from discover import StormAudioDiscovery
from media_player import StormAudioMediaPlayer
from setup import StormAudioSetupFlow
from ucapi import EntityTypes, media_player
from ucapi_framework import BaseConfigManager, BaseIntegrationDriver, get_config_path


class StormAudioIntegrationDriver(
    BaseIntegrationDriver[StormAudioDevice, StormAudioConfig]
):
    """StormAudio Integration Driver."""

    def __init__(self):
        """Initialize the integration driver."""
        super().__init__(
            device_class=StormAudioDevice,
            entity_classes=[StormAudioMediaPlayer],
            require_connection_before_registry=True,
        )

    async def refresh_entity_state(self, entity_id):
        """Refresh the state of a configured entity by querying the device."""
        await super().refresh_entity_state(entity_id)

        device_id = self.device_from_entity_id(entity_id)
        if device_id is None:
            logging.getLogger(Loggers.DRIVER).debug(
                "Entity %s is not a device entity", entity_id
            )
            return

        device = self._configured_devices.get(device_id)
        if device is None:
            logging.getLogger(Loggers.DRIVER).warning(
                "Device %s not found for entity %s", device_id, entity_id
            )
            return

        configured_entity = self.api.configured_entities.get(entity_id)
        if configured_entity is None:
            logging.getLogger(Loggers.DRIVER).debug(
                "Entity %s is not configured, ignoring", entity_id
            )
            return

        match configured_entity.entity_type:
            case EntityTypes.MEDIA_PLAYER:
                self.api.configured_entities.update_attributes(
                    entity_id,
                    {
                        media_player.Attributes.SOURCE_LIST: device.source_list,
                        media_player.Attributes.SOUND_MODE_LIST: device.sound_mode_list,
                    },
                )

    async def async_register_available_entities(
        self, device_config: StormAudioConfig, device: StormAudioDevice
    ) -> None:
        """Register available entities for a device (async version)."""
        entity = StormAudioMediaPlayer(
            config_device=device_config,
            device_instance=device,
        )

        self.api.available_entities.add(entity)


async def main():
    """Start the Remote Two integration driver."""
    logging.basicConfig()

    # Configure logging level from environment variable
    level = os.getenv("UC_LOG_LEVEL", "DEBUG").upper()
    logging.getLogger(Loggers.DRIVER).setLevel(level)
    logging.getLogger(Loggers.MEDIA_PLAYER).setLevel(level)
    logging.getLogger(Loggers.DEVICE).setLevel(level)
    logging.getLogger(Loggers.SETUP_FLOW).setLevel(level)

    # Initialize the integration driver
    driver = StormAudioIntegrationDriver()

    # Configure the device config manager
    driver.config_manager = BaseConfigManager(
        get_config_path(driver.api.config_dir_path),
        driver.on_device_added,
        driver.on_device_removed,
        config_class=StormAudioConfig,
    )

    # Register all configured devices from config file
    await driver.register_all_configured_devices()

    # Set up device discovery (optional - remove if not using discovery)
    discovery = StormAudioDiscovery(timeout=5, service_type="_stormremote._tcp.local.")
    setup_handler = StormAudioSetupFlow.create_handler(driver, discovery=discovery)

    # Initialize the API with the driver configuration
    await driver.api.init("driver.json", setup_handler)

    # Keep the driver running
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
