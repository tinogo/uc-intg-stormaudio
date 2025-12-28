"""
Setup Flow Module.

This module handles the device setup and configuration process. It provides
forms for manual device entry and validation of device connections.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from device import StormAudioDevice
from typing import Any

from const import StormAudioConfig
from ucapi import IntegrationSetupError, RequestUserInput, SetupError
from ucapi_framework import BaseSetupFlow

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
                            "Please enter the connection details for your device."
                        ),
                    }
                }
            },
        },
        {
            "field": {"text": {"value": ""}},
            "id": "name",
            "label": {
                "en": "Device Name",
            },
        },
        {
            "field": {"text": {"value": ""}},
            "id": "address",
            "label": {
                "en": "IP Address or Hostname",
            },
        },
    ],
)


class DeviceSetupFlow(BaseSetupFlow[StormAudioConfig]):
    """
    Setup flow for device integration.

    Handles device configuration through discovery or manual entry.
    Extend this class to add custom setup logic for your device.
    """

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
        name = input_values.get("name", "").strip()
        address = input_values.get("address", "").strip()

        # Validate required fields
        if not address:
            _LOG.warning("Address is required, re-displaying form")
            return _MANUAL_INPUT_SCHEMA

        # Use a default name if not provided
        if not name:
            name = f"Device ({address})"

        _LOG.debug("Attempting to connect to device at %s", address)

        try:
            client = StormAudioDevice(address)
            await client.connect()

            return StormAudioConfig(
                identifier=input_values.get("name", address.replace(".", "_")),
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
