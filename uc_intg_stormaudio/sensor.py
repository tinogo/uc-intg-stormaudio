"""
Sensor Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from typing import Any

from ucapi import EntityTypes, Sensor
from ucapi.sensor import Attributes as SensorAttr
from ucapi.sensor import DeviceClasses, Options, States
from ucapi_framework import Entity, create_entity_id

from uc_intg_stormaudio.const import (
    SENSOR_STATE_MAPPING,
    Loggers,
    SensorType,
    StormAudioStates,
)
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
    SensorType.AUDIO_STREAM: "Audio Stream",
    SensorType.AURO_PRESET: "Auro-Matic Preset",
    SensorType.AURO_STRENGTH: "Auro-Matic Strength",
    SensorType.DOLBY_MODE: "Dolby mode",
    SensorType.HDMI_1_VIDEO_STREAM: "HDMI-Out 1 Video Stream",
    SensorType.HDMI_2_VIDEO_STREAM: "HDMI-Out 2 Video Stream",
    SensorType.LOUDNESS: "Loudness",
    SensorType.PRESET: "Preset",
    SensorType.SOURCE: "Source",
    SensorType.UPMIXER_MODE: "Upmixer",
}

_binary_sensors = {
    SensorType.DOLBY_CENTER_SPREAD: "Dolby Center Spread",
    SensorType.DOLBY_VIRTUALIZER: "Dolby Virtualizer",
    SensorType.MUTE: "Mute",
    SensorType.STORM_XT: "StormXT",
}


class StormAudioSensor(Sensor, Entity):  # pylint: disable=too-few-public-methods
    """Sensor for the StormAudio ISPs."""

    def __init__(self, device: StormAudioDevice, sensor_type: SensorType):
        """Initialize the sensor entity."""
        self._device = device
        self._sensor_type = sensor_type

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

        self.subscribe_to_device(device)

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

    def map_entity_states(self, device_state: StormAudioStates) -> States:
        """Convert a device-specific state to a UC API entity state."""
        return SENSOR_STATE_MAPPING[device_state]

    async def sync_state(self) -> None:  # pylint: disable=too-many-branches
        """Update the sensor attributes."""
        if self._sensor_type == SensorType.AUDIO_STREAM:
            self.update(self._get_audio_stream_sensor_attributes())
        elif self._sensor_type == SensorType.AURO_PRESET:
            self.update(self._get_auro_preset_sensor_attributes())
        elif self._sensor_type == SensorType.AURO_STRENGTH:
            self.update(self._get_auro_strength_sensor_attributes())
        elif self._sensor_type == SensorType.BASS_DB:
            self.update(self._get_bass_sensor_attributes())
        elif self._sensor_type == SensorType.BRIGHTNESS_DB:
            self.update(self._get_brightness_sensor_attributes())
        elif self._sensor_type == SensorType.CENTER_ENHANCE_DB:
            self.update(self._get_center_enhance_sensor_attributes())
        elif self._sensor_type == SensorType.DOLBY_CENTER_SPREAD:
            self.update(self._get_dolby_center_spread_sensor_attributes())
        elif self._sensor_type == SensorType.DOLBY_MODE:
            self.update(self._get_dolby_mode_sensor_attributes())
        elif self._sensor_type == SensorType.DOLBY_VIRTUALIZER:
            self.update(self._get_dolby_virtualizer_sensor_attributes())
        elif self._sensor_type == SensorType.HDMI_1_VIDEO_STREAM:
            self.update(self._get_hdmi_out_1_video_stream_sensor_attributes())
        elif self._sensor_type == SensorType.HDMI_2_VIDEO_STREAM:
            self.update(self._get_hdmi_out_2_video_stream_sensor_attributes())
        elif self._sensor_type == SensorType.LFE_ENHANCE_DB:
            self.update(self._get_lfe_enhance_sensor_attributes())
        elif self._sensor_type == SensorType.LOUDNESS:
            self.update(self._get_loudness_sensor_attributes())
        elif self._sensor_type == SensorType.MUTE:
            self.update(self._get_mute_sensor_attributes())
        elif self._sensor_type == SensorType.PRESET:
            self.update(self._get_preset_sensor_attributes())
        elif self._sensor_type == SensorType.SOURCE:
            self.update(self._get_source_sensor_attributes())
        elif self._sensor_type == SensorType.STORM_XT:
            self.update(self._get_storm_xt_sensor_attributes())
        elif self._sensor_type == SensorType.SURROUND_ENHANCE_DB:
            self.update(self._get_surround_enhance_sensor_attributes())
        elif self._sensor_type == SensorType.TREBLE_DB:
            self.update(self._get_treble_sensor_attributes())
        elif self._sensor_type == SensorType.UPMIXER_MODE:
            self.update(self._get_upmixer_mode_sensor_attributes())
        elif self._sensor_type == SensorType.VOLUME_DB:
            self.update(self._get_volume_sensor_attributes())
        else:
            raise ValueError(f"Unsupported sensor type: {self._sensor_type}")

    def _get_audio_stream_sensor_attributes(self) -> dict[str, Any]:
        """Get the current Audio stream sensor attributes."""
        values = [
            self._device.device_attributes.audio_stream,
            self._device.device_attributes.audio_format,
            self._device.device_attributes.audio_sample_rate,
        ]
        # Filter out falsy values (None, empty string, etc.)
        filtered_values = [str(v) for v in values if v]

        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: ", ".join(filtered_values)
            if self._device.device_attributes.audio_stream != "None"
            else "-",
        }

    def _get_auro_preset_sensor_attributes(self) -> dict[str, Any]:
        """Get the Auro-Matic preset sensor attributes."""
        if self._device.device_attributes.actual_upmixer_mode_id != 4:
            return {
                SensorAttr.STATE: SENSOR_STATE_MAPPING[StormAudioStates.UNAVAILABLE],
                SensorAttr.VALUE: None,
            }

        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: str(self._device.device_attributes.auro_preset),
        }

    def _get_auro_strength_sensor_attributes(self) -> dict[str, Any]:
        """Get the Auro-Matic strength sensor attributes."""
        if self._device.device_attributes.actual_upmixer_mode_id != 4:
            return {
                SensorAttr.STATE: SENSOR_STATE_MAPPING[StormAudioStates.UNAVAILABLE],
                SensorAttr.VALUE: None,
            }

        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: str(self._device.device_attributes.auro_strength),
        }

    def _get_bass_sensor_attributes(self) -> dict[str, Any]:
        """Get the bass sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: str(self._device.device_attributes.bass),
            SensorAttr.UNIT: "dB",
        }

    def _get_brightness_sensor_attributes(self) -> dict[str, Any]:
        """Get the brightness sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: str(self._device.device_attributes.brightness),
            SensorAttr.UNIT: "dB",
        }

    def _get_center_enhance_sensor_attributes(self) -> dict[str, Any]:
        """Get the center-enhance sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: str(self._device.device_attributes.center_enhance),
            SensorAttr.UNIT: "dB",
        }

    def _get_dolby_center_spread_sensor_attributes(self) -> dict[str, Any]:
        """Get the Dolby Center Spread sensor attributes."""
        if self._device.device_attributes.actual_upmixer_mode_id != 2:
            return {
                SensorAttr.STATE: SENSOR_STATE_MAPPING[StormAudioStates.UNAVAILABLE],
                SensorAttr.VALUE: None,
            }

        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: "on"
            if self._device.device_attributes.dolby_center_spread
            else "off",
            SensorAttr.UNIT: "sound",
        }

    def _get_dolby_mode_sensor_attributes(self) -> dict[str, Any]:
        """Get the volume sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: self._device.device_attributes.dolby_mode,
        }

    def _get_dolby_virtualizer_sensor_attributes(self) -> dict[str, Any]:
        """Get the Dolby virtualizer sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: "on"
            if self._device.device_attributes.dolby_virtualizer
            else "off",
            SensorAttr.UNIT: "sound",
        }

    def _get_hdmi_out_1_video_stream_sensor_attributes(self) -> dict[str, Any]:
        """Get the current HDMI-Out 1 video stream sensor attributes."""
        input_name = self._device.device_attributes.hdmi_1.get("input_name")
        timing = self._device.device_attributes.hdmi_1.get("timing")
        copy_protection = self._device.device_attributes.hdmi_1.get("copy_protection")
        color_space = self._device.device_attributes.hdmi_1.get("color_space")
        color_depth = self._device.device_attributes.hdmi_1.get("color_depth")
        mode = self._device.device_attributes.hdmi_1.get("mode")
        hdr = self._device.device_attributes.hdmi_1.get("hdr")

        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: f"{timing}, {copy_protection}, {color_space}, {color_depth}, {mode}, {hdr}"
            if input_name != "-" and input_name is not None
            else "-",
        }

    def _get_hdmi_out_2_video_stream_sensor_attributes(self) -> dict[str, Any]:
        """Get the current HDMI-Out 2 video stream sensor attributes."""
        input_name = self._device.device_attributes.hdmi_2.get("input_name")
        timing = self._device.device_attributes.hdmi_2.get("timing")
        copy_protection = self._device.device_attributes.hdmi_2.get("copy_protection")
        color_space = self._device.device_attributes.hdmi_2.get("color_space")
        color_depth = self._device.device_attributes.hdmi_2.get("color_depth")
        mode = self._device.device_attributes.hdmi_2.get("mode")
        hdr = self._device.device_attributes.hdmi_2.get("hdr")

        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: f"{timing}, {copy_protection}, {color_space}, {color_depth}, {mode}, {hdr}"
            if input_name != "-" and input_name is not None
            else "-",
        }

    def _get_lfe_enhance_sensor_attributes(self) -> dict[str, Any]:
        """Get the LFE-enhance sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: str(self._device.device_attributes.lfe_enhance),
            SensorAttr.UNIT: "dB",
        }

    def _get_loudness_sensor_attributes(self) -> dict[str, Any]:
        """Get the loudness sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: self._device.device_attributes.loudness,
        }

    def _get_mute_sensor_attributes(self) -> dict[str, Any]:
        """Get the mute sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: "on" if self._device.device_attributes.muted else "off",
            SensorAttr.UNIT: "sound",
        }

    def _get_preset_sensor_attributes(self) -> dict[str, Any]:
        """Get the preset sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: self._device.device_attributes.preset,
        }

    def _get_source_sensor_attributes(self) -> dict[str, Any]:
        """Get the source sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: self._device.device_attributes.source,
        }

    def _get_storm_xt_sensor_attributes(self) -> dict[str, Any]:
        """Get the StormXT sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: "on"
            if self._device.device_attributes.storm_xt_active
            else "off",
            SensorAttr.UNIT: "sound",
        }

    def _get_surround_enhance_sensor_attributes(self) -> dict[str, Any]:
        """Get the surround-enhance sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: str(self._device.device_attributes.surround_enhance),
            SensorAttr.UNIT: "dB",
        }

    def _get_treble_sensor_attributes(self) -> dict[str, Any]:
        """Get the treble sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: str(self._device.device_attributes.treble),
            SensorAttr.UNIT: "dB",
        }

    def _get_upmixer_mode_sensor_attributes(self) -> dict[str, Any]:
        """Get the volume sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: self._device.device_attributes.actual_sound_mode,
        }

    def _get_volume_sensor_attributes(self) -> dict[str, Any]:
        """Get the volume sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self._device.state],
            SensorAttr.VALUE: str(self._device.device_attributes.volume - 100),
            SensorAttr.UNIT: "dB",
        }
