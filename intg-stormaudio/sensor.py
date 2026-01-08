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


class StormAudioSensor(Sensor):  # pylint: disable=too-few-public-methods
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
            attributes=sensor_config['attributes'],
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
                sensor_entity_id = create_entity_id(
                    EntityTypes.SENSOR,
                    device.identifier,
                    SensorType.VOLUME_DB.value,
                )
                sensor = {
                    "identifier": sensor_entity_id,
                    "name": f"{device.name} Volume",
                    "device_class": DeviceClasses.CUSTOM,
                    "options": {
                        Options.CUSTOM_UNIT: "dB",
                        Options.DECIMALS: 1,
                    },
                    "attributes": self._device.get_device_attributes(sensor_entity_id),
                }

            case SensorType.UPMIXER_MODE:
                sensor_entity_id = create_entity_id(
                    EntityTypes.SENSOR,
                    device.identifier,
                    SensorType.UPMIXER_MODE.value,
                )
                sensor = {
                    "identifier": sensor_entity_id,
                    "name": f"{device.name} Upmixer",
                    "device_class": DeviceClasses.CUSTOM,
                    "attributes": self._device.get_device_attributes(sensor_entity_id),
                }

            case SensorType.MUTE:
                sensor_entity_id = create_entity_id(
                    EntityTypes.SENSOR,
                    device.identifier,
                    SensorType.MUTE.value,
                )
                sensor = {
                    "identifier": sensor_entity_id,
                    "name": f"{device.name} Mute",
                    "device_class": DeviceClasses.BINARY,
                    "attributes": self._device.get_device_attributes(sensor_entity_id),
                }

            case SensorType.STORM_XT:
                sensor_entity_id = create_entity_id(
                    EntityTypes.SENSOR,
                    device.identifier,
                    SensorType.STORM_XT.value,
                )
                sensor = {
                    "identifier": sensor_entity_id,
                    "name": f"{device.name} StormXT",
                    "device_class": DeviceClasses.BINARY,
                    "attributes": self._device.get_device_attributes(sensor_entity_id),
                }

            case _:
                raise ValueError(f"Unsupported sensor type: {sensor_type}")
        return sensor


def create_sensors(device: StormAudioDevice) -> list[StormAudioSensor]:
    """Create all applicable sensor entities for the given ISP."""
    sensors = []
    for sensor_type in SensorType:
        sensors.append(StormAudioSensor(device, sensor_type))
    return sensors
