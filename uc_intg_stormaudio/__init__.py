"""
Remote Two/3 Integration Driver.

This is the main entry point for the integration driver. It initializes
the driver, sets up logging, and starts the integration API.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import asyncio
import logging
import os

from ucapi_framework import BaseConfigManager, BaseIntegrationDriver, get_config_path

from uc_intg_stormaudio.config import StormAudioConfig
from uc_intg_stormaudio.const import Loggers, SensorType
from uc_intg_stormaudio.device import StormAudioDevice
from uc_intg_stormaudio.discover import StormAudioDiscovery
from uc_intg_stormaudio.media_player import StormAudioMediaPlayer
from uc_intg_stormaudio.remote import StormAudioRemote
from uc_intg_stormaudio.select import StormAudioSelect
from uc_intg_stormaudio.sensor import StormAudioSensor
from uc_intg_stormaudio.setup import StormAudioSetupFlow


async def main():
    """Start the Remote Two integration driver."""
    logging.basicConfig()

    # Configure logging level from environment variable
    level = os.getenv("UC_LOG_LEVEL", "DEBUG").upper()
    for logger in Loggers:
        logging.getLogger(logger).setLevel(level)

    # Initialize the integration driver
    integration_driver = BaseIntegrationDriver(
        device_class=StormAudioDevice,
        entity_classes=[
            StormAudioMediaPlayer,
            StormAudioRemote,
            StormAudioSelect,
            lambda device_config, dev: [
                StormAudioSensor(dev, sensor_type) for sensor_type in SensorType
            ],
        ],
    )

    # Configure the device config manager
    integration_driver.config_manager = BaseConfigManager(
        get_config_path(integration_driver.api.config_dir_path),
        integration_driver.on_device_added,
        integration_driver.on_device_removed,
        config_class=StormAudioConfig,
    )

    # Register all configured devices from config file
    await integration_driver.register_all_device_instances(True)

    # Set up device discovery (optional - remove if not using discovery)
    discovery = StormAudioDiscovery(timeout=5, service_type="_stormremote._tcp.local.")
    setup_handler = StormAudioSetupFlow.create_handler(
        driver=integration_driver, discovery=discovery
    )

    # Initialize the API with the driver configuration
    await integration_driver.api.init("driver.json", setup_handler)

    # Keep the driver running
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
