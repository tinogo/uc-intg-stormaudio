"""
Sensor Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any

from ucapi import EntityTypes, Sensor
from ucapi.sensor import DeviceClasses, Options
from ucapi_framework import Entity, create_entity_id

from uc_intg_stormaudio.const import Loggers, SensorType
from uc_intg_stormaudio.device import StormAudioDevice

_LOG = logging.getLogger(Loggers.SENSOR)

_decibel_based_custom_sensors = {
    SensorType.BASS_DB: "Bass",
    SensorType.BRIGHTNESS_DB: "Brightness",
    SensorType.CENTER_ENHANCE_DB: "Center enhance",
    SensorType.LFE_ENHANCE_DB: "LFE enhance",
    SensorType.LOUDNESS: "Loudness",
    SensorType.SURROUND_ENHANCE_DB: "Surround enhance",
    SensorType.TREBLE_DB: "Treble",
    SensorType.VOLUME_DB: "Volume",
}

_simple_custom_sensors = {
    SensorType.DOLBY_MODE: "Dolby mode",
    SensorType.LOUDNESS: "Loudness",
    SensorType.PRESET: "Preset",
    SensorType.SOURCE: "Source",
    SensorType.UPMIXER_MODE: "Upmixer",
}

_binary_sensors = {
    SensorType.MUTE: "Mute",
    SensorType.STORM_XT: "StormXT",
}


class StormAudioSensor(Sensor, Entity):  # pylint: disable=too-few-public-methods
    """Sensor for the StormAudio ISPs."""

    def __init__(self, device: StormAudioDevice, sensor_type: SensorType):
        """Initialize the sensor entity."""
        self._device = device

        sensor_config = self._get_sensor_config(sensor_type, device)

        _LOG.debug("Initializing sensor: %s", sensor_config["identifier"])

        super().__init__(
            identifier=sensor_config["identifier"],
            name=sensor_config["name"],
            features=[],
            attributes=sensor_config["attributes"],
            device_class=sensor_config["device_class"],
            options=sensor_config.get("options", {}),
        )

    def _get_sensor_config(
        self, sensor_type: SensorType, device: StormAudioDevice
    ) -> dict[str, Any]:
        """Get sensor configuration based on type."""
        sensor = {}
        sensor_entity_id = create_entity_id(
            EntityTypes.SENSOR,
            device.identifier,
            sensor_type,
        )

        match sensor_type:
            case sensor_type if (
                _decibel_based_custom_sensors.get(sensor_type) is not None
            ):
                sensor = {
                    "identifier": sensor_entity_id,
                    "name": f"{device.name} Sensor: {_decibel_based_custom_sensors.get(sensor_type)}",
                    "device_class": DeviceClasses.CUSTOM,
                    "options": {
                        Options.CUSTOM_UNIT: "dB",
                        Options.DECIMALS: 1,
                    },
                    "attributes": self._device.get_device_attributes(sensor_entity_id),
                }

            case sensor_type if _simple_custom_sensors.get(sensor_type) is not None:
                sensor = {
                    "identifier": sensor_entity_id,
                    "name": f"{device.name} Sensor: {_simple_custom_sensors.get(sensor_type)}",
                    "device_class": DeviceClasses.CUSTOM,
                    "attributes": self._device.get_device_attributes(sensor_entity_id),
                }

            case sensor_type if _binary_sensors.get(sensor_type) is not None:
                sensor = {
                    "identifier": sensor_entity_id,
                    "name": f"{device.name} Sensor: {_binary_sensors.get(sensor_type)}",
                    "device_class": DeviceClasses.BINARY,
                    "attributes": self._device.get_device_attributes(sensor_entity_id),
                }

            case _:
                raise ValueError(f"Unsupported sensor type: {sensor_type}")
        return sensor
