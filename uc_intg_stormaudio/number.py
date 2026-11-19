"""
Number Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from ucapi import EntityTypes, Number, StatusCodes
from ucapi.number import Attributes as NumberAttr
from ucapi.number import Commands as NumberCommands
from ucapi.number import DeviceClasses, Options
from ucapi.number import States as NumberStates
from ucapi_framework import Entity, create_entity_id

from uc_intg_stormaudio.const import (
    Loggers,
    StormAudioStates,
)
from uc_intg_stormaudio.device import (
    MAX_TONE_CONTROL,
    MIN_TONE_CONTROL,
    StormAudioDevice,
)

_LOG = logging.getLogger(Loggers.NUMBER)

_TONE_CONTROL_STEP = 1

_TONE_CONTROL_NUMBER_OPTIONS = {
    Options.MIN: MIN_TONE_CONTROL,
    Options.MAX: MAX_TONE_CONTROL,
    Options.STEP: _TONE_CONTROL_STEP,
    Options.DECIMALS: 0,
}


class NumberType(StrEnum):
    """Defines the supported number types for StormAudio devices."""

    BASS = "bass"
    BRIGHTNESS = "brightness"
    CENTER_ENHANCE = "center_enhance"
    LFE_ENHANCE = "lfe_enhance"
    SURROUND_ENHANCE = "surround_enhance"
    TREBLE = "treble"


NUMBER_STATE_MAPPING = {
    StormAudioStates.ON: NumberStates.ON,
    StormAudioStates.OFF: NumberStates.UNAVAILABLE,
    StormAudioStates.UNAVAILABLE: NumberStates.UNAVAILABLE,
    StormAudioStates.UNKNOWN: NumberStates.UNKNOWN,
}


@dataclass(frozen=True)
class NumberEntityConfig:
    """Defines all behavior required to build and handle a number entity."""

    name: str
    device_class: DeviceClasses
    value_getter: Callable[[StormAudioDevice], float | None]
    setter: Callable[[StormAudioDevice, float], Awaitable[None]]
    options: dict[str, Any]


@dataclass(frozen=True)
class ResolvedNumberConfig:
    """Resolved config payload used for number initialization."""

    identifier: str
    name: str
    attributes: Any
    entity_config: NumberEntityConfig


NUMBER_ENTITY_CONFIG: dict[NumberType, NumberEntityConfig] = {
    NumberType.BASS: NumberEntityConfig(
        name="Bass",
        device_class=DeviceClasses.AUDIO_LEVEL,
        value_getter=lambda device: device.device_attributes.bass,
        setter=lambda device, value: device.bass_x(int(value)),
        options=_TONE_CONTROL_NUMBER_OPTIONS,
    ),
    NumberType.BRIGHTNESS: NumberEntityConfig(
        name="Brightness",
        device_class=DeviceClasses.AUDIO_LEVEL,
        value_getter=lambda device: device.device_attributes.brightness,
        setter=lambda device, value: device.brightness_x(int(value)),
        options=_TONE_CONTROL_NUMBER_OPTIONS,
    ),
    NumberType.CENTER_ENHANCE: NumberEntityConfig(
        name="Center enhance",
        device_class=DeviceClasses.AUDIO_LEVEL,
        value_getter=lambda device: device.device_attributes.center_enhance,
        setter=lambda device, value: device.center_enhance_x(int(value)),
        options=_TONE_CONTROL_NUMBER_OPTIONS,
    ),
    NumberType.LFE_ENHANCE: NumberEntityConfig(
        name="LFE enhance",
        device_class=DeviceClasses.AUDIO_LEVEL,
        value_getter=lambda device: device.device_attributes.lfe_enhance,
        setter=lambda device, value: device.lfe_enhance_x(int(value)),
        options=_TONE_CONTROL_NUMBER_OPTIONS,
    ),
    NumberType.SURROUND_ENHANCE: NumberEntityConfig(
        name="Surround enhance",
        device_class=DeviceClasses.AUDIO_LEVEL,
        value_getter=lambda device: device.device_attributes.surround_enhance,
        setter=lambda device, value: device.surround_enhance_x(int(value)),
        options=_TONE_CONTROL_NUMBER_OPTIONS,
    ),
    NumberType.TREBLE: NumberEntityConfig(
        name="Treble",
        device_class=DeviceClasses.AUDIO_LEVEL,
        value_getter=lambda device: device.device_attributes.treble,
        setter=lambda device, value: device.treble_x(int(value)),
        options=_TONE_CONTROL_NUMBER_OPTIONS,
    ),
}


class StormAudioNumber(Number, Entity):
    """Number-Entity for the StormAudio ISPs."""

    def __init__(self, device: StormAudioDevice, number_type: NumberType):
        """Initialize the number entity."""
        self._device = device

        number_config = self._get_number_config(number_type, device)
        self._entity_config = number_config.entity_config

        _LOG.debug("Initializing number: %s", number_config.identifier)

        super().__init__(
            identifier=number_config.identifier,
            name=number_config.name,
            features=[],
            attributes=number_config.attributes,
            device_class=self._entity_config.device_class,
            options=self._entity_config.options,
            cmd_handler=self.handle_command,
        )

        self.subscribe_to_device(device)

    def _get_number_config(
        self, number_type: NumberType, device: StormAudioDevice
    ) -> ResolvedNumberConfig:
        """Get number configuration based on type."""
        config = NUMBER_ENTITY_CONFIG.get(number_type)
        if config is None:
            raise ValueError(f"Unsupported number type: {number_type}")
        number_entity_id = create_entity_id(
            EntityTypes.NUMBER,
            device.identifier,
            number_type,
        )

        return ResolvedNumberConfig(
            identifier=number_entity_id,
            name=f"{device.name} Number: {config.name}",
            attributes=self._device.get_device_attributes(number_entity_id),
            entity_config=config,
        )

    async def handle_command(
        self,
        entity: Number,
        cmd_id: str,
        params: dict[str, Any] | None,
        _: Any | None = None,
    ) -> StatusCodes:
        """Handle number commands from the remote."""
        _LOG.debug(
            "[%s] Received command for number entity: %s %s",
            entity.id,
            cmd_id,
            params if params else "",
        )

        params = params or {}

        try:
            match cmd_id:
                case NumberCommands.SET_VALUE:
                    if "value" not in params:
                        return StatusCodes.BAD_REQUEST
                    value = float(params["value"])
                case NumberCommands.INCREMENT:
                    value = self._get_current_value() + self._get_step(params)
                case NumberCommands.DECREMENT:
                    value = self._get_current_value() - self._get_step(params)
                case _:
                    return StatusCodes.NOT_IMPLEMENTED
        except TypeError, ValueError:
            return StatusCodes.BAD_REQUEST

        await self._entity_config.setter(self._device, self._clamp(value))
        return StatusCodes.OK

    def _get_current_value(self) -> float:
        value = self._entity_config.value_getter(self._device)
        return float(value) if value is not None else 0.0

    def _get_step(self, params: dict[str, Any]) -> float:
        return float(params.get("step", self._entity_config.options[Options.STEP]))

    def _clamp(self, value: float) -> float:
        options = self._entity_config.options
        return max(options[Options.MIN], min(options[Options.MAX], value))

    def map_entity_states(self, device_state: StormAudioStates) -> NumberStates:
        """Convert a device-specific state to a UC API entity state."""
        return NUMBER_STATE_MAPPING[device_state]

    async def sync_state(self) -> None:
        """Update the number attributes."""
        state = NUMBER_STATE_MAPPING[self._device.state]
        value = (
            self._entity_config.value_getter(self._device)
            if state == NumberStates.ON
            else None
        )
        self.update(
            {
                NumberAttr.STATE: state,
                NumberAttr.VALUE: value,
            }
        )
