import logging
from typing import Any

from ucapi import Sensor, EntityTypes
from ucapi.sensor import DeviceClasses, Options, Attributes, States
from ucapi_framework import create_entity_id

from const import Loggers, SensorType
from device import StormAudioDevice

_LOG = logging.getLogger(Loggers.SENSOR)


class StormAudioSensor(Sensor):
    def __init__(self, device_instance: StormAudioDevice, sensor_type: SensorType):
        self._device = device_instance

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
                    "unit": "dB",
                    "options": {
                        Options.CUSTOM_UNIT: "dB",
                        Options.DECIMALS: 1,
                    },
                }

            case SensorType.MUTE:
                sensor = {
                    "identifier": create_entity_id(
                        EntityTypes.SENSOR, device.identifier, SensorType.MUTE.value
                    ),
                    "name": f"{device.name} Mute Status",
                    "device_class": DeviceClasses.BINARY,
                }

            case _:
                raise ValueError(f"Unsupported sensor type: {sensor_type}")
        return sensor


def create_sensors(device: StormAudioDevice) -> list[StormAudioSensor]:
    """Create all applicable sensor entities for the given ISP."""
    return [
        StormAudioSensor(device, SensorType.VOLUME_DB),
        StormAudioSensor(device, SensorType.MUTE),
    ]
