"""
Setup Flow Module.

This module handles the device setup and configuration process. It provides
forms for manual device entry and validation of device connections.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any

from const import StormAudioConfig
from ucapi import IntegrationSetupError, RequestUserInput, SetupError
from ucapi_framework import BaseSetupFlow, DiscoveredDevice

_LOG = logging.getLogger(__name__)

# This form is displayed when the user chooses manual device entry
_MANUAL_INPUT_SCHEMA = RequestUserInput(
    {"en": "StormAudio Setup"},
    [
        {
            "id": "info",
            "label": {
                "en": "Setup your StormAudio processor",
            },
            "field": {
                "label": {
                    "value": {
                        "en": (
                            "Please enter the IP Address of your StormAudio processor/receiver."
                        ),
                        "de": (
                            "Bitte gebe die IP-Adresse deines StormAudio Prozessors/Receivers an."
                        ),
                    }
                }
            },
        },
        {
            "field": {"text": {"value": ""}},
            "id": "address",
            "label": {
                "en": "IP Address",
                "de": "IP-Adresse",
            },
        },
    ],
)


class StormAudioSetupFlow(BaseSetupFlow[StormAudioConfig]):
    """
    Setup flow for device integration.

    Handles device configuration through discovery or manual entry.
    Extend this class to add custom setup logic for your device.
    """

    async def discover_devices(self) -> list[DiscoveredDevice]:
        if self.discovery:
            return await self.discovery.discover()
        return []

    async def prepare_input_from_discovery(
        self, device: DiscoveredDevice, additional_input: dict[str, Any]
    ) -> dict[str, Any]:
        """Convert discovered device to input values."""
        return {
            "identifier": device.identifier,
            "name": device.name,
            "address": device.address,
        }

    def get_manual_entry_form(self) -> RequestUserInput:
        """
        Return the manual entry form for device setup.

        Override this method to return a custom form for your device.

        :return: RequestUserInput with form fields for manual configuration
        """
        return _MANUAL_INPUT_SCHEMA

    async def query_device(
        self, input_values: dict[str, Any]
    ) -> StormAudioConfig | SetupError | RequestUserInput:
        """
        Create device configuration from user input.

        This method is called after the user submits the setup form.
        It should validate the input, attempt to connect to the device,
        and return a DeviceConfig if successful.

        :param input_values: Dictionary of user input from the form
        :return: DeviceConfig on success, SetupError on failure, or
                 RequestUserInput to re-display the form
        """
        # Extract form values
        address = input_values.get("address", "").strip()

        # Validate required fields
        if not address:
            _LOG.warning("Address is required, re-displaying form")
            return _MANUAL_INPUT_SCHEMA

        name = f"StormAudio ISP ({address})"

        _LOG.debug("Attempting to connect to device at %s", address)

        try:
            return StormAudioConfig(
                identifier=address.replace(".", "_"),
                name=name,
                address=address,
            )

        except ConnectionError as ex:
            _LOG.error("Connection refused to %s: %s", address, ex)
            return SetupError(IntegrationSetupError.CONNECTION_REFUSED)

        except TimeoutError as ex:
            _LOG.error("Connection timeout to %s: %s", address, ex)
            return SetupError(IntegrationSetupError.TIMEOUT)

        except Exception as ex:
            _LOG.error("Failed to connect to %s: %s", address, ex)
            _LOG.info("Please verify the device address and try again")
            return SetupError(IntegrationSetupError.CONNECTION_REFUSED)
