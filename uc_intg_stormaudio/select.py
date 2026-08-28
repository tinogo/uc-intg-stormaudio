"""
Select Entity.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import logging
from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Generic, Literal, TypeVar, cast

from ucapi import EntityTypes, Select, StatusCodes
from ucapi.select import Attributes as SelectAttr
from ucapi.select import Commands as SelectCommands
from ucapi.select import States as SelectStates
from ucapi_framework import Entity, create_entity_id

from uc_intg_stormaudio.const import (
    Loggers,
    StormAudioStates,
)
from uc_intg_stormaudio.device import StormAudioDevice

_LOG = logging.getLogger(Loggers.SELECT)


SelectOption = str | int
OptionT = TypeVar("OptionT", bound=SelectOption)


class SelectType(StrEnum):
    """Defines the supported select types for StormAudio devices."""

    AURO_PRESET = "auro_preset"
    AURO_STRENGTH = "auro_strength"
    PRESET = "preset"
    SOUND_MODE = "sound_mode"


SELECT_STATE_MAPPING = {
    StormAudioStates.ON: SelectStates.ON,
    StormAudioStates.OFF: SelectStates.UNAVAILABLE,
    StormAudioStates.UNAVAILABLE: SelectStates.UNAVAILABLE,
    StormAudioStates.UNKNOWN: SelectStates.UNKNOWN,
}


class CommandMode(StrEnum):
    """Supported command execution strategies for select entities."""

    LIST_NAVIGATION = "list_navigation"
    DEVICE_NAVIGATION = "device_navigation"


@dataclass(frozen=True)
class SelectEntityConfig(Generic[OptionT]):
    """Defines all behavior required to build and handle a select entity."""

    name: str
    options_getter: Callable[[StormAudioDevice], Sequence[OptionT]]
    current_navigation_getter: Callable[[StormAudioDevice], OptionT | None]
    current_display_getter: Callable[[StormAudioDevice], SelectOption | None]
    setter: Callable[[StormAudioDevice, OptionT], Awaitable[Any]]
    option_parser: Callable[[Any], OptionT | None]
    command_mode: CommandMode = CommandMode.LIST_NAVIGATION
    next_command: Callable[[StormAudioDevice], Awaitable[Any]] | None = None
    previous_command: Callable[[StormAudioDevice], Awaitable[Any]] | None = None
    is_available: Callable[[StormAudioDevice], bool] | None = None


@dataclass(frozen=True)
class ResolvedSelectConfig:
    """Resolved config payload used for entity initialization."""

    identifier: str
    name: str
    attributes: Any
    entity_config: SelectEntityConfig[Any]


def _parse_string_option(option: Any) -> str | None:
    if isinstance(option, str):
        return option
    return None


def _parse_int_option(option: Any) -> int | None:
    if isinstance(option, bool):
        return None
    if isinstance(option, int):
        return option
    if isinstance(option, str):
        try:
            return int(option)
        except ValueError:
            return None
    return None


def _format_int_as_string(value: Any) -> str | None:
    if value is None:
        return None
    return str(value)


def _is_auro_upmixer_active(device: StormAudioDevice) -> bool:
    return device.device_attributes.actual_upmixer_mode_id == 4


SELECT_ENTITY_CONFIG: dict[SelectType, SelectEntityConfig] = {
    SelectType.AURO_PRESET: SelectEntityConfig(
        name="Auro-Matic Preset",
        options_getter=lambda device: device.device_attributes.auro_preset_list,
        current_navigation_getter=lambda device: device.device_attributes.auro_preset,
        current_display_getter=lambda device: device.device_attributes.auro_preset,
        setter=lambda device, option: device.auro_preset_x(option),
        option_parser=_parse_string_option,
        is_available=_is_auro_upmixer_active,
    ),
    SelectType.AURO_STRENGTH: SelectEntityConfig(
        name="Auro-Matic Strength",
        options_getter=lambda device: device.device_attributes.auro_strength_list,
        current_navigation_getter=lambda device: device.device_attributes.auro_strength,
        current_display_getter=lambda device: _format_int_as_string(
            device.device_attributes.auro_strength
        ),
        setter=lambda device, option: device.auro_strength_x(option),
        option_parser=_parse_int_option,
        is_available=_is_auro_upmixer_active,
    ),
    SelectType.PRESET: SelectEntityConfig(
        name="Preset",
        options_getter=lambda device: device.device_attributes.preset_list,
        current_navigation_getter=lambda device: device.device_attributes.preset,
        current_display_getter=lambda device: device.device_attributes.preset,
        setter=lambda device, option: device.preset_x(option),
        option_parser=_parse_string_option,
        command_mode=CommandMode.DEVICE_NAVIGATION,
        next_command=lambda device: device.preset_next(),
        previous_command=lambda device: device.preset_prev(),
    ),
    SelectType.SOUND_MODE: SelectEntityConfig(
        name="Sound mode",
        options_getter=lambda device: device.device_attributes.sound_mode_list,
        current_navigation_getter=lambda device: device.device_attributes.sound_mode,
        current_display_getter=lambda device: (
            device.device_attributes.actual_sound_mode
        ),
        setter=lambda device, option: device.select_sound_mode(option),
        option_parser=_parse_string_option,
    ),
}


class StormAudioSelect(Select, Entity):
    """Select for the StormAudio ISPs."""

    def __init__(
        self,
        device: StormAudioDevice,
        select_type: SelectType,
    ):
        """Initialize the select entity."""
        self._device = device
        select_config = self._get_select_config(select_type, device)
        self._config: SelectEntityConfig[Any] = select_config.entity_config

        _LOG.debug("Initializing select: %s", select_config.identifier)

        super().__init__(
            identifier=select_config.identifier,
            name=select_config.name,
            attributes=select_config.attributes,
            cmd_handler=self.handle_command,
        )

        self.subscribe_to_device(device)

    def _get_select_config(
        self, select_type: SelectType, device: StormAudioDevice
    ) -> ResolvedSelectConfig:
        """Get select configuration based on type."""
        config = SELECT_ENTITY_CONFIG.get(select_type)
        if config is None:
            raise ValueError(f"Unsupported select type: {select_type}")

        select_entity_id = create_entity_id(
            EntityTypes.SELECT,
            device.identifier,
            select_type,
        )

        return ResolvedSelectConfig(
            identifier=select_entity_id,
            name=f"{device.name} Select: {config.name}",
            attributes=self._device.get_device_attributes(select_entity_id),
            entity_config=config,
        )

    async def handle_command(
        self,
        entity: Select,
        cmd_id: str,
        params: dict[str, Any] | None,
        _: Any | None = None,
    ) -> StatusCodes:
        """Handle select commands from the remote."""
        _LOG.debug(
            "[%s] Received command for select entity: %s %s",
            entity.id,
            cmd_id,
            params if params else "",
        )

        if self._config.command_mode == CommandMode.DEVICE_NAVIGATION:
            return await self._handle_device_navigation_command(cmd_id, params)

        return await self._handle_list_navigation_command(cmd_id, params)

    @staticmethod
    def _get_command_cycle(params: dict[str, Any] | None) -> bool:
        return bool((params or {}).get("cycle", False))

    @staticmethod
    def _get_command_option(params: dict[str, Any] | None) -> Any | None:
        return (params or {}).get("option")

    def _is_available(self) -> bool:
        if self._config.is_available is None:
            return True
        return self._config.is_available(self._device)

    def _get_options(self) -> Sequence[SelectOption]:
        return self._config.options_getter(self._device)

    def _get_current_option_value(self) -> SelectOption | None:
        return self._config.current_display_getter(self._device)

    async def _call_setter(self, option: SelectOption) -> None:
        await self._config.setter(self._device, option)

    async def _handle_list_navigation_command(
        self,
        cmd_id: str,
        params: dict[str, Any] | None,
    ) -> Literal[StatusCodes.OK]:
        """Handle list-based select commands for any configured select type."""
        options = self._get_options()
        if not options:
            return StatusCodes.OK

        command_handlers: dict[str, Callable[[], Awaitable[None]]] = {
            SelectCommands.SELECT_OPTION: lambda: self._handle_list_select_option(
                params
            ),
            SelectCommands.SELECT_FIRST: lambda: self._call_setter(options[0]),
            SelectCommands.SELECT_LAST: lambda: self._call_setter(options[-1]),
            SelectCommands.SELECT_NEXT: lambda: self._handle_list_select_next(
                options, params
            ),
            SelectCommands.SELECT_PREVIOUS: lambda: self._handle_list_select_previous(
                options, params
            ),
        }

        handler = command_handlers.get(cmd_id)
        if handler is not None:
            await handler()

        return StatusCodes.OK

    async def _handle_list_select_option(self, params: dict[str, Any] | None) -> None:
        option = self._get_command_option(params)
        parsed_option = self._config.option_parser(option)
        if parsed_option is not None:
            await self._call_setter(cast(SelectOption, parsed_option))

    async def _handle_list_select_next(
        self,
        options: Sequence[SelectOption],
        params: dict[str, Any] | None,
    ) -> None:
        current_option = self._config.current_navigation_getter(self._device)
        if current_option is None or current_option not in options:
            return

        current_index = options.index(current_option)
        if current_index < len(options) - 1:
            await self._call_setter(options[current_index + 1])
        elif self._get_command_cycle(params):
            await self._call_setter(options[0])

    async def _handle_list_select_previous(
        self,
        options: Sequence[SelectOption],
        params: dict[str, Any] | None,
    ) -> None:
        current_option = self._config.current_navigation_getter(self._device)
        if current_option is None or current_option not in options:
            return

        current_index = options.index(current_option)
        if current_index > 0:
            await self._call_setter(options[current_index - 1])
        elif self._get_command_cycle(params):
            await self._call_setter(options[-1])

    async def _handle_device_navigation_command(
        self,
        cmd_id: str,
        params: dict[str, Any] | None,
    ) -> Literal[StatusCodes.OK]:
        """Handle selects that use dedicated next/previous device methods."""
        options = self._get_options()

        command_handlers: dict[str, Callable[[], Awaitable[None]]] = {
            SelectCommands.SELECT_OPTION: lambda: self._handle_device_select_option(
                params
            ),
            SelectCommands.SELECT_FIRST: lambda: self._handle_device_select_first(
                options
            ),
            SelectCommands.SELECT_LAST: lambda: self._handle_device_select_last(
                options
            ),
            SelectCommands.SELECT_NEXT: self._handle_device_select_next,
            SelectCommands.SELECT_PREVIOUS: self._handle_device_select_previous,
        }

        handler = command_handlers.get(cmd_id)
        if handler is not None:
            await handler()

        return StatusCodes.OK

    async def _handle_device_select_option(self, params: dict[str, Any] | None) -> None:
        option = self._get_command_option(params)
        parsed_option = self._config.option_parser(option)
        if parsed_option is not None:
            await self._call_setter(cast(SelectOption, parsed_option))

    async def _handle_device_select_first(
        self, options: Sequence[SelectOption]
    ) -> None:
        if options:
            await self._call_setter(options[0])

    async def _handle_device_select_last(self, options: Sequence[SelectOption]) -> None:
        if options:
            await self._call_setter(options[-1])

    async def _handle_device_select_next(self) -> None:
        if self._config.next_command is not None:
            await self._config.next_command(self._device)

    async def _handle_device_select_previous(self) -> None:
        if self._config.previous_command is not None:
            await self._config.previous_command(self._device)

    def map_entity_states(self, device_state: StormAudioStates) -> SelectStates:
        """Convert a device-specific state to a UC API entity state."""
        return SELECT_STATE_MAPPING[device_state]

    async def sync_state(self) -> None:
        """Update the select attributes."""
        self.update(self._get_select_attributes())

    def _get_select_attributes(self) -> dict[str, Any]:
        """Build select attributes from configuration and current device state."""
        if not self._is_available():
            return {
                SelectAttr.STATE: SELECT_STATE_MAPPING[StormAudioStates.UNAVAILABLE],
                SelectAttr.CURRENT_OPTION: None,
                SelectAttr.OPTIONS: [],
            }

        current_option = self._get_current_option_value()
        options = self._get_options()

        return {
            SelectAttr.STATE: SELECT_STATE_MAPPING[self._device.state],
            SelectAttr.CURRENT_OPTION: current_option,
            SelectAttr.OPTIONS: options,
        }
