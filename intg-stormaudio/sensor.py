"""
Sensor Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any

from const import Loggers, SensorType
from device import StormAudioDevice
from ucapi import EntityTypes, Sensor
from ucapi.sensor import Attributes, DeviceClasses, Options, States
from ucapi_framework import create_entity_id

_LOG = logging.getLogger(Loggers.SENSOR)


class StormAudioSensor(Sensor):
    """Sensor for the StormAudio ISPs."""

    def __init__(self, device_instance: StormAudioDevice, sensor_type: SensorType):
        """Initialize the sensor entity."""
        self._device = device_instance
        self._sensor_type = sensor_type

        sensor_config = self._get_sensor_config(sensor_type, device_instance)

        _LOG.debug("Initializing sensor: %s", sensor_config["identifier"])

        super().__init__(
            identifier=sensor_config["identifier"],
            name=sensor_config["name"],
            features=[],
            attributes={
                Attributes.STATE: States.UNAVAILABLE,
                Attributes.VALUE: None,
                Attributes.UNIT: sensor_config.get("unit"),
            },
            device_class=sensor_config["device_class"],
            options=sensor_config.get("options", {}),
        )

    def _get_sensor_config(
        self, sensor_type: SensorType, device: StormAudioDevice
    ) -> dict[str, Any]:
        """Get sensor configuration based on type."""
        sensor = {}
        match sensor_type:
            case SensorType.VOLUME_DB:
                sensor = {
                    "identifier": create_entity_id(
                        EntityTypes.SENSOR,
                        device.identifier,
                        SensorType.VOLUME_DB.value,
                    ),
                    "name": f"{device.name} Volume",
                    "device_class": DeviceClasses.CUSTOM,
                    "options": {
                        Options.CUSTOM_UNIT: "dB",
                        Options.DECIMALS: 1,
                    },
                    "attributes": self.get_sensor_attributes(),
                }

            case SensorType.MUTE:
                sensor = {
                    "identifier": create_entity_id(
                        EntityTypes.SENSOR, device.identifier, SensorType.MUTE.value
                    ),
                    "name": f"{device.name} Mute Status",
                    "device_class": DeviceClasses.BINARY,
                    "attributes": self.get_sensor_attributes(),
                }

            case _:
                raise ValueError(f"Unsupported sensor type: {sensor_type}")
        return sensor

    def get_sensor_attributes(self) -> dict[str, Any]:
        """Get sensor attributes based on type."""
        match self._sensor_type:
            case SensorType.VOLUME_DB:
                return {
                    Attributes.STATE: States.ON
                    if self._device.state == States.ON
                    else States.UNAVAILABLE,
                    Attributes.VALUE: self._device.volume - 100,
                    Attributes.UNIT: "dB",
                }

            case SensorType.MUTE:
                return {
                    Attributes.STATE: States.ON
                    if self._device.state == States.ON
                    else States.UNAVAILABLE,
                    Attributes.VALUE: "on" if self._device.muted else "off",
                }


def create_sensors(device: StormAudioDevice) -> list[StormAudioSensor]:
    """Create all applicable sensor entities for the given ISP."""
    return [
        StormAudioSensor(device, SensorType.VOLUME_DB),
        StormAudioSensor(device, SensorType.MUTE),
    ]
