"""
Sensor Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Callable

from ucapi import EntityTypes, Sensor
from ucapi.sensor import Attributes as SensorAttr
from ucapi.sensor import DeviceClasses, Options
from ucapi.sensor import States as SensorStates
from ucapi_framework import Entity, create_entity_id

from uc_intg_stormaudio.const import (
    Loggers,
    StormAudioStates,
)
from uc_intg_stormaudio.device import StormAudioDevice

_LOG = logging.getLogger(Loggers.SENSOR)

_DB_SENSOR_OPTIONS = {
    Options.CUSTOM_UNIT: "dB",
    Options.DECIMALS: 1,
}


class SensorType(StrEnum):
    """Defines the supported sensor types for StormAudio devices."""

    AUDIO_STREAM = "audio_stream"
    AURO_PRESET = "auro_preset"
    AURO_STRENGTH = "auro_strength"
    BASS_DB = "bass_db"
    BRIGHTNESS_DB = "brightness_db"
    CENTER_ENHANCE_DB = "center_enhance_db"
    DOLBY_MODE = "dolby_mode"
    DOLBY_CENTER_SPREAD = "dolby_center_spread"
    DOLBY_VIRTUALIZER = "dolby_virtualizer"
    HDMI_1_VIDEO_STREAM = "hdmi_1_video_stream"
    HDMI_2_VIDEO_STREAM = "hdmi_2_video_stream"
    LFE_ENHANCE_DB = "lfe_enhance_db"
    LOUDNESS = "loudness"
    MUTE = "mute"
    PRESET = "preset"
    SOURCE = "source"
    STORM_XT = "storm_xt"
    SURROUND_ENHANCE_DB = "surround_enhance_db"
    TREBLE_DB = "treble_db"
    UPMIXER_MODE = "upmixer"
    VOLUME_DB = "volume_db"


SENSOR_STATE_MAPPING = {
    StormAudioStates.ON: SensorStates.ON,
    StormAudioStates.OFF: SensorStates.UNAVAILABLE,
    StormAudioStates.UNAVAILABLE: SensorStates.UNAVAILABLE,
    StormAudioStates.UNKNOWN: SensorStates.UNKNOWN,
}


@dataclass(frozen=True)
class SensorEntityConfig:
    """Defines all behavior required to build and handle a sensor entity."""

    name: str
    device_class: DeviceClasses
    attributes_getter: Callable[[StormAudioDevice], dict[str, Any]]
    options: dict[str, Any] | None = None


@dataclass(frozen=True)
class ResolvedSensorConfig:
    """Resolved config payload used for sensor initialization."""

    identifier: str
    name: str
    device_class: DeviceClasses
    attributes: Any
    options: dict[str, Any]
    entity_config: SensorEntityConfig


def _build_sensor_attributes(
    device: StormAudioDevice,
    value: Any,
    unit: str | None = None,
) -> dict[str, Any]:
    attributes = {
        SensorAttr.STATE: SENSOR_STATE_MAPPING[device.state],
        SensorAttr.VALUE: value,
    }
    if unit is not None:
        attributes[SensorAttr.UNIT] = unit
    return attributes


def _build_unavailable_sensor_attributes() -> dict[str, Any]:
    return {
        SensorAttr.STATE: SENSOR_STATE_MAPPING[StormAudioStates.UNAVAILABLE],
        SensorAttr.VALUE: None,
    }


def _is_auro_upmixer_active(device: StormAudioDevice) -> bool:
    return device.device_attributes.actual_upmixer_mode_id == 4


def _is_dolby_upmixer_active(device: StormAudioDevice) -> bool:
    return device.device_attributes.actual_upmixer_mode_id == 2


def _format_on_off(value: bool) -> str:
    return "on" if value else "off"


def _get_audio_stream_value(device: StormAudioDevice) -> str:
    values = [
        device.device_attributes.audio_stream,
        device.device_attributes.audio_format,
        device.device_attributes.audio_sample_rate,
    ]
    filtered_values = [str(v) for v in values if v]

    if device.device_attributes.audio_stream == "None":
        return "-"
    return ", ".join(filtered_values)


def _get_hdmi_video_stream_value(hdmi: dict[str, str | None]) -> str:
    input_name = hdmi.get("input_name")
    if input_name in (None, "-"):
        return "-"

    values = [
        hdmi.get("timing"),
        hdmi.get("copy_protection"),
        hdmi.get("color_space"),
        hdmi.get("color_depth"),
        hdmi.get("mode"),
        hdmi.get("hdr"),
    ]
    return ", ".join(str(v) for v in values)


SENSOR_ENTITY_CONFIG: dict[SensorType, SensorEntityConfig] = {
    SensorType.AUDIO_STREAM: SensorEntityConfig(
        name="Audio Stream",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            _get_audio_stream_value(device),
        ),
    ),
    SensorType.AURO_PRESET: SensorEntityConfig(
        name="Auro-Matic Preset",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: (
            _build_sensor_attributes(device, str(device.device_attributes.auro_preset))
            if _is_auro_upmixer_active(device)
            else _build_unavailable_sensor_attributes()
        ),
    ),
    SensorType.AURO_STRENGTH: SensorEntityConfig(
        name="Auro-Matic Strength",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: (
            _build_sensor_attributes(
                device, str(device.device_attributes.auro_strength)
            )
            if _is_auro_upmixer_active(device)
            else _build_unavailable_sensor_attributes()
        ),
    ),
    SensorType.BASS_DB: SensorEntityConfig(
        name="Bass",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            str(device.device_attributes.bass),
            unit="dB",
        ),
        options=_DB_SENSOR_OPTIONS,
    ),
    SensorType.BRIGHTNESS_DB: SensorEntityConfig(
        name="Brightness",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            str(device.device_attributes.brightness),
            unit="dB",
        ),
        options=_DB_SENSOR_OPTIONS,
    ),
    SensorType.CENTER_ENHANCE_DB: SensorEntityConfig(
        name="Center enhance",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            str(device.device_attributes.center_enhance),
            unit="dB",
        ),
        options=_DB_SENSOR_OPTIONS,
    ),
    SensorType.DOLBY_CENTER_SPREAD: SensorEntityConfig(
        name="Dolby Center Spread",
        device_class=DeviceClasses.BINARY,
        attributes_getter=lambda device: (
            _build_sensor_attributes(
                device,
                _format_on_off(device.device_attributes.dolby_center_spread),
                unit="sound",
            )
            if _is_dolby_upmixer_active(device)
            else _build_unavailable_sensor_attributes()
        ),
    ),
    SensorType.DOLBY_MODE: SensorEntityConfig(
        name="Dolby mode",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            device.device_attributes.dolby_mode,
        ),
    ),
    SensorType.DOLBY_VIRTUALIZER: SensorEntityConfig(
        name="Dolby Virtualizer",
        device_class=DeviceClasses.BINARY,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            _format_on_off(device.device_attributes.dolby_virtualizer),
            unit="sound",
        ),
    ),
    SensorType.HDMI_1_VIDEO_STREAM: SensorEntityConfig(
        name="HDMI-Out 1 Video Stream",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            _get_hdmi_video_stream_value(device.device_attributes.hdmi_1),
        ),
    ),
    SensorType.HDMI_2_VIDEO_STREAM: SensorEntityConfig(
        name="HDMI-Out 2 Video Stream",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            _get_hdmi_video_stream_value(device.device_attributes.hdmi_2),
        ),
    ),
    SensorType.LFE_ENHANCE_DB: SensorEntityConfig(
        name="LFE enhance",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            str(device.device_attributes.lfe_enhance),
            unit="dB",
        ),
        options=_DB_SENSOR_OPTIONS,
    ),
    SensorType.LOUDNESS: SensorEntityConfig(
        name="Loudness",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            device.device_attributes.loudness,
        ),
        options=_DB_SENSOR_OPTIONS,
    ),
    SensorType.MUTE: SensorEntityConfig(
        name="Mute",
        device_class=DeviceClasses.BINARY,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            _format_on_off(device.device_attributes.muted),
            unit="sound",
        ),
    ),
    SensorType.PRESET: SensorEntityConfig(
        name="Preset",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            device.device_attributes.preset,
        ),
    ),
    SensorType.SOURCE: SensorEntityConfig(
        name="Source",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            device.device_attributes.source,
        ),
    ),
    SensorType.STORM_XT: SensorEntityConfig(
        name="StormXT",
        device_class=DeviceClasses.BINARY,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            _format_on_off(device.device_attributes.storm_xt_active),
            unit="sound",
        ),
    ),
    SensorType.SURROUND_ENHANCE_DB: SensorEntityConfig(
        name="Surround enhance",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            str(device.device_attributes.surround_enhance),
            unit="dB",
        ),
        options=_DB_SENSOR_OPTIONS,
    ),
    SensorType.TREBLE_DB: SensorEntityConfig(
        name="Treble",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            str(device.device_attributes.treble),
            unit="dB",
        ),
        options=_DB_SENSOR_OPTIONS,
    ),
    SensorType.UPMIXER_MODE: SensorEntityConfig(
        name="Upmixer",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            device.device_attributes.actual_sound_mode,
        ),
    ),
    SensorType.VOLUME_DB: SensorEntityConfig(
        name="Volume",
        device_class=DeviceClasses.CUSTOM,
        attributes_getter=lambda device: _build_sensor_attributes(
            device,
            str(device.device_attributes.volume - 100),
            unit="dB",
        ),
        options=_DB_SENSOR_OPTIONS,
    ),
}


class StormAudioSensor(Sensor, Entity):  # pylint: disable=too-few-public-methods
    """Sensor for the StormAudio ISPs."""

    def __init__(self, device: StormAudioDevice, sensor_type: SensorType):
        """Initialize the sensor entity."""
        self._device = device

        sensor_config = self._get_sensor_config(sensor_type, device)
        self._entity_config = sensor_config.entity_config

        _LOG.debug("Initializing sensor: %s", sensor_config.identifier)

        super().__init__(
            identifier=sensor_config.identifier,
            name=sensor_config.name,
            features=[],
            attributes=sensor_config.attributes,
            device_class=sensor_config.device_class,
            options=sensor_config.options,
        )

        self.subscribe_to_device(device)

    def _get_sensor_config(
        self, sensor_type: SensorType, device: StormAudioDevice
    ) -> ResolvedSensorConfig:
        """Get sensor configuration based on type."""
        config = SENSOR_ENTITY_CONFIG.get(sensor_type)
        if config is None:
            raise ValueError(f"Unsupported sensor type: {sensor_type}")
        sensor_entity_id = create_entity_id(
            EntityTypes.SENSOR,
            device.identifier,
            sensor_type,
        )

        return ResolvedSensorConfig(
            identifier=sensor_entity_id,
            name=f"{device.name} Sensor: {config.name}",
            device_class=config.device_class,
            options=config.options or {},
            attributes=self._device.get_device_attributes(sensor_entity_id),
            entity_config=config,
        )

    def map_entity_states(self, device_state: StormAudioStates) -> SensorStates:
        """Convert a device-specific state to a UC API entity state."""
        return SENSOR_STATE_MAPPING[device_state]

    async def sync_state(self) -> None:
        """Update the sensor attributes."""
        self.update(self._entity_config.attributes_getter(self._device))
