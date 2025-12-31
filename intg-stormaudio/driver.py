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
from ucapi_framework import BaseConfigManager, BaseIntegrationDriver, get_config_path


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
    driver = BaseIntegrationDriver(
        device_class=StormAudioDevice, entity_classes=[StormAudioMediaPlayer]
    )

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
