"""
Device Communication Module.

This module handles all communication with your device. It manages connections,
sends commands, and tracks the device state.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

import json
import logging
from typing import Any, Callable

from ucapi import EntityTypes
from ucapi.media_player import Attributes as MediaAttr
from ucapi.remote import Attributes as RemoteAttr
from ucapi.select import Attributes as SelectAttr
from ucapi.sensor import Attributes as SensorAttr
from ucapi_framework import PersistentConnectionDevice, create_entity_id
from ucapi_framework.device import DeviceEvents

from uc_intg_stormaudio.const import (
    MEDIA_PLAYER_STATE_MAPPING,
    REMOTE_STATE_MAPPING,
    SELECT_STATE_MAPPING,
    SENSOR_STATE_MAPPING,
    Loggers,
    SelectType,
    SensorType,
    StormAudioCommands,
    StormAudioResponses,
    StormAudioStates,
)
from uc_intg_stormaudio.device_attributes import StormAudioDeviceAttributes
from uc_intg_stormaudio.helpers import fix_json
from uc_intg_stormaudio.stormaudio import StormAudioClient

_LOG = logging.getLogger(Loggers.DEVICE)

MIN_VOLUME = 0
MAX_VOLUME = 100
MAX_TIME_OUT = 9  # the current command timeout is 10 seconds. Therefore, we need to be below that threshold.


class StormAudioDevice(PersistentConnectionDevice):
    """StormAudio Device."""

    def __init__(self, *args, **kwargs):
        """Initialize the device."""
        super().__init__(*args, **kwargs)

        self.device_attributes: StormAudioDeviceAttributes = (
            StormAudioDeviceAttributes()
        )

        self._client = StormAudioClient(self.address, self.device_config.port)

        self._entity_attributes: dict[str, Callable] = {
            create_entity_id(
                EntityTypes.MEDIA_PLAYER, self.identifier
            ): self._get_media_player_attributes,
            create_entity_id(
                EntityTypes.REMOTE, self.identifier
            ): self._get_remote_attributes,
            create_entity_id(
                EntityTypes.SELECT, self.identifier, SelectType.AURO_PRESET.value
            ): self._get_auro_preset_select_attributes,
            create_entity_id(
                EntityTypes.SELECT, self.identifier, SelectType.AURO_STRENGTH.value
            ): self._get_auro_strength_select_attributes,
            create_entity_id(
                EntityTypes.SELECT, self.identifier, SelectType.PRESET.value
            ): self._get_preset_select_attributes,
            create_entity_id(
                EntityTypes.SELECT, self.identifier, SelectType.SOUND_MODE.value
            ): self._get_sound_mode_select_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.AURO_PRESET.value
            ): self._get_auro_preset_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.AURO_STRENGTH.value
            ): self._get_auro_strength_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.BASS_DB.value
            ): self._get_bass_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.BRIGHTNESS_DB.value
            ): self._get_brightness_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.CENTER_ENHANCE_DB.value
            ): self._get_center_enhance_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.DOLBY_MODE.value
            ): self._get_dolby_mode_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.LFE_ENHANCE_DB.value
            ): self._get_lfe_enhance_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.LOUDNESS.value
            ): self._get_loudness_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.MUTE.value
            ): self._get_mute_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.PRESET.value
            ): self._get_preset_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.SOURCE.value
            ): self._get_source_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.STORM_XT.value
            ): self._get_storm_xt_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR,
                self.identifier,
                SensorType.SURROUND_ENHANCE_DB.value,
            ): self._get_surround_enhance_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.TREBLE_DB.value
            ): self._get_treble_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.UPMIXER_MODE.value
            ): self._get_upmixer_mode_sensor_attributes,
            create_entity_id(
                EntityTypes.SENSOR, self.identifier, SensorType.VOLUME_DB.value
            ): self._get_volume_sensor_attributes,
        }

    @property
    def address(self) -> str | None:
        """Return the device address."""
        return self._device_config.address

    @property
    def identifier(self) -> str:
        """Return the device identifier."""
        return self._device_config.identifier

    @property
    def log_id(self) -> str:
        """Return a log identifier for debugging."""
        return self.name if self.name else self.identifier

    @property
    def name(self) -> str:
        """Return the device name."""
        return self._device_config.name

    @property
    def state(self) -> StormAudioStates:
        """Return the current device state."""
        return self.device_attributes.state

    async def establish_connection(self) -> Any:
        """Establish connection to the device."""
        return await self._client.connect()

    async def close_connection(self) -> None:
        """Close the connection."""
        if self._connection:
            await self._client.close(self._connection)

    async def maintain_connection(self) -> None:  # pylint: disable=too-many-statements
        """Maintain the connection."""  # noqa: D202

        # pylint: disable=too-many-branches,too-many-locals,too-many-statements
        def message_handler(message: str) -> None:
            match message:
                case message if message.startswith(StormAudioResponses.DOLBY_MODE_X):
                    dolby_mode, *_tail = json.loads(
                        message[len(StormAudioResponses.DOLBY_MODE_X) :]  # noqa: E203
                    )
                    self.device_attributes.dolby_mode_id = dolby_mode
                    self._update_attributes()

                case StormAudioResponses.INPUT_LIST_START:
                    self.device_attributes.sources = {}

                case message if message.startswith(StormAudioResponses.INPUT_LIST_X):
                    input_name, input_id, *_tail = json.loads(
                        fix_json(
                            message[len(StormAudioResponses.INPUT_LIST_X) :]  # noqa: E203
                        )
                    )

                    self.device_attributes.sources.update({input_name: input_id})

                case StormAudioResponses.INPUT_LIST_END:
                    self.update_config(sources=self.device_attributes.sources)
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.INPUT_X):
                    source_id, *_tail = json.loads(
                        fix_json(
                            message[len(StormAudioResponses.INPUT_X) :]  # noqa: E203
                        )
                    )
                    self.device_attributes.source_id = source_id
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.LOUDNESS_X):
                    loudness, *_tail = json.loads(
                        message[len(StormAudioResponses.LOUDNESS_X) :]  # noqa: E203
                    )
                    self.device_attributes.loudness_mode_id = loudness
                    self._update_attributes()

                case StormAudioResponses.MUTE_ON | StormAudioResponses.MUTE_OFF:
                    muted = message == StormAudioResponses.MUTE_ON
                    self.device_attributes.muted = muted
                    self._update_attributes()

                case StormAudioResponses.PRESET_LIST_START:
                    self.device_attributes.presets = {}

                case message if message.startswith(StormAudioResponses.PRESET_LIST_X):
                    preset_name, preset_id, *_tail = json.loads(
                        fix_json(
                            message[len(StormAudioResponses.PRESET_LIST_X) :]  # noqa: E203
                        )
                    )

                    self.device_attributes.presets.update({preset_name: preset_id})

                case StormAudioResponses.PRESET_LIST_END:
                    self.update_config(presets=self.device_attributes.presets)
                    self._update_attributes()

                case message if message.startswith(
                    StormAudioResponses.PRESET_X
                ) and not message.startswith(StormAudioResponses.PRESET_CUSTOM_X):
                    preset_id, *_tail = json.loads(
                        fix_json(
                            message[len(StormAudioResponses.PRESET_X) :]  # noqa: E203
                        )
                    )
                    self.device_attributes.preset_id = preset_id
                    self._update_attributes()

                case (
                    StormAudioResponses.PROC_STATE_OFF
                    | StormAudioResponses.PROC_STATE_INDETERMINATE
                ):
                    # Maps both the initialization and the process of shutting down to OFF
                    # as they are not "fully booted"
                    self.device_attributes.state = StormAudioStates.OFF
                    self._update_attributes()

                case StormAudioResponses.PROC_STATE_ON:
                    self.device_attributes.state = StormAudioStates.ON
                    self._update_attributes()

                case StormAudioResponses.STORM_XT_ON | StormAudioResponses.STORM_XT_OFF:
                    storm_xt_active = message == StormAudioResponses.STORM_XT_ON
                    self.device_attributes.storm_xt_active = storm_xt_active
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.SURROUND_MODE_X):
                    upmixer_mode_id, *_tail = json.loads(
                        fix_json(
                            message[len(StormAudioResponses.SURROUND_MODE_X) :]  # noqa: E203
                        )
                    )
                    self.device_attributes.upmixer_mode_id = upmixer_mode_id
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.ALLOWED_MODE_X):
                    actual_upmixer_mode_id, *_tail = json.loads(
                        fix_json(
                            message[len(StormAudioResponses.ALLOWED_MODE_X) :]  # noqa: E203
                        )
                    )
                    self.device_attributes.actual_upmixer_mode_id = (
                        actual_upmixer_mode_id
                    )
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.VOLUME_X):
                    # The UC remotes currently only support absolute volume scales.
                    # That's why we need to convert the relative values from the ISPs.
                    volume, *_tail = json.loads(
                        message[len(StormAudioResponses.VOLUME_X) :]  # noqa: E203
                    )
                    absolute_volume = int(volume) + MAX_VOLUME
                    self.device_attributes.volume = absolute_volume
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.BASS_X):
                    bass, *_tail = json.loads(
                        message[len(StormAudioResponses.BASS_X) :]  # noqa: E203
                    )
                    self.device_attributes.bass = bass
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.TREBLE_X):
                    treble, *_tail = json.loads(
                        message[len(StormAudioResponses.TREBLE_X) :]  # noqa: E203
                    )
                    self.device_attributes.treble = treble
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.BRIGHTNESS_X):
                    brightness, *_tail = json.loads(
                        message[len(StormAudioResponses.BRIGHTNESS_X) :]  # noqa: E203
                    )
                    self.device_attributes.brightness = brightness
                    self._update_attributes()

                case message if message.startswith(
                    StormAudioResponses.CENTER_ENHANCE_X
                ):
                    center_enhance, *_tail = json.loads(
                        message[len(StormAudioResponses.CENTER_ENHANCE_X) :]  # noqa: E203
                    )
                    self.device_attributes.center_enhance = center_enhance
                    self._update_attributes()

                case message if message.startswith(
                    StormAudioResponses.SURROUND_ENHANCE_X
                ):
                    surround_enhance, *_tail = json.loads(
                        message[len(StormAudioResponses.SURROUND_ENHANCE_X) :]  # noqa: E203
                    )
                    self.device_attributes.surround_enhance = surround_enhance
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.LFE_ENHANCE_X):
                    lfe_enhance, *_tail = json.loads(
                        message[len(StormAudioResponses.LFE_ENHANCE_X) :]  # noqa: E203
                    )
                    self.device_attributes.lfe_enhance = lfe_enhance
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.AURO_PRESET_X):
                    auro_preset_id, *_tail = json.loads(
                        message[len(StormAudioResponses.AURO_PRESET_X) :]  # noqa: E203
                    )
                    self.device_attributes.auro_preset_id = auro_preset_id
                    self._update_attributes()

                case message if message.startswith(StormAudioResponses.AURO_STRENGTH_X):
                    auro_strength, *_tail = json.loads(
                        message[len(StormAudioResponses.AURO_STRENGTH_X) :]  # noqa: E203
                    )
                    self.device_attributes.auro_strength = auro_strength
                    self._update_attributes()

        await self._client.parse_response_messages(self._connection, message_handler)

    async def _send_command(self, command: str) -> None:
        """Send a command to the device."""
        if not self._connection:
            _LOG.error("[%s] Cannot send command, not connected", self.log_id)
            return

        await self._client.send_command(self._connection, command)

    async def _wait_for_response(
        self, pattern: str, timeout: float = 5.0, prefix_match: bool = False
    ) -> str | None:
        return await self._client.wait_for_response(pattern, timeout, prefix_match)

    def _update_attributes(self) -> None:
        """Update the device attributes via an event."""
        self._update_media_player_attributes()
        self._update_remote_attributes()
        self._update_select_attributes()
        self._update_sensor_attributes()

    def _update_media_player_attributes(self) -> None:
        """Update the media player attributes via an event."""
        media_player_entity_id = create_entity_id(
            EntityTypes.MEDIA_PLAYER, self.identifier
        )
        self.events.emit(
            DeviceEvents.UPDATE,
            media_player_entity_id,
            self.get_device_attributes(media_player_entity_id),
        )

    def _update_remote_attributes(self) -> None:
        """Update the remote attributes via an event."""
        remote_entity_id = create_entity_id(EntityTypes.REMOTE, self.identifier)
        self.events.emit(
            DeviceEvents.UPDATE,
            remote_entity_id,
            self.get_device_attributes(remote_entity_id),
        )

    def _update_select_attributes(self) -> None:
        """Update the select attributes via an event."""
        for select_type in SelectType:
            select_entity_id = create_entity_id(
                EntityTypes.SELECT, self.identifier, select_type
            )

            self.events.emit(
                DeviceEvents.UPDATE,
                select_entity_id,
                self.get_device_attributes(select_entity_id),
            )

    def _update_sensor_attributes(self) -> None:
        """Update the sensor attributes via an event."""
        for sensor_type in SensorType:
            sensor_entity_id = create_entity_id(
                EntityTypes.SENSOR, self.identifier, sensor_type
            )

            self.events.emit(
                DeviceEvents.UPDATE,
                sensor_entity_id,
                self.get_device_attributes(sensor_entity_id),
            )

    def get_device_attributes(self, entity_id: str) -> dict[str, Any]:
        """Get the device attributes for the given entity ID."""
        return self._entity_attributes[entity_id]()

    def _get_media_player_attributes(self) -> dict[str, Any]:
        """Get the media player attributes."""
        return {
            MediaAttr.STATE: MEDIA_PLAYER_STATE_MAPPING[self.state],
            MediaAttr.SOURCE: self.device_attributes.source,
            MediaAttr.SOURCE_LIST: self.device_attributes.source_list,
            MediaAttr.SOUND_MODE: self.device_attributes.actual_sound_mode,
            MediaAttr.SOUND_MODE_LIST: self.device_attributes.sound_mode_list,
            MediaAttr.VOLUME: self.device_attributes.volume,
            MediaAttr.MUTED: self.device_attributes.muted,
        }

    def _get_auro_preset_select_attributes(self) -> dict[str, Any]:
        """Get the Auro-Matic preset select attributes."""
        return {
            SelectAttr.STATE: SELECT_STATE_MAPPING[self.state],
            SelectAttr.CURRENT_OPTION: self.device_attributes.auro_preset,
            SelectAttr.OPTIONS: self.device_attributes.auro_preset_list,
        }

    def _get_auro_strength_select_attributes(self) -> dict[str, Any]:
        """Get the Auro-Matic strength select attributes."""
        return {
            SelectAttr.STATE: SELECT_STATE_MAPPING[self.state],
            SelectAttr.CURRENT_OPTION: str(self.device_attributes.auro_strength),
            SelectAttr.OPTIONS: self.device_attributes.auro_strength_list,
        }

    def _get_preset_select_attributes(self) -> dict[str, Any]:
        """Get the preset select attributes."""
        return {
            SelectAttr.STATE: SELECT_STATE_MAPPING[self.state],
            SelectAttr.CURRENT_OPTION: self.device_attributes.preset,
            SelectAttr.OPTIONS: self.device_attributes.preset_list,
        }

    def _get_sound_mode_select_attributes(self) -> dict[str, Any]:
        """Get the preset select attributes."""
        return {
            SelectAttr.STATE: SELECT_STATE_MAPPING[self.state],
            SelectAttr.CURRENT_OPTION: self.device_attributes.actual_sound_mode,
            SelectAttr.OPTIONS: self.device_attributes.sound_mode_list,
        }

    def _get_remote_attributes(self) -> dict[str, Any]:
        """Get the remote attributes."""
        return {
            RemoteAttr.STATE: REMOTE_STATE_MAPPING[self.state],
        }

    def _get_auro_preset_sensor_attributes(self) -> dict[str, Any]:
        """Get the Auro-Matic preset sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: str(self.device_attributes.auro_preset),
        }

    def _get_auro_strength_sensor_attributes(self) -> dict[str, Any]:
        """Get the Auro-Matic strength sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: str(self.device_attributes.auro_strength),
        }

    def _get_bass_sensor_attributes(self) -> dict[str, Any]:
        """Get the bass sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: str(self.device_attributes.bass),
            SensorAttr.UNIT: "dB",
        }

    def _get_brightness_sensor_attributes(self) -> dict[str, Any]:
        """Get the brightness sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: str(self.device_attributes.brightness),
            SensorAttr.UNIT: "dB",
        }

    def _get_center_enhance_sensor_attributes(self) -> dict[str, Any]:
        """Get the center-enhance sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: str(self.device_attributes.center_enhance),
            SensorAttr.UNIT: "dB",
        }

    def _get_dolby_mode_sensor_attributes(self) -> dict[str, Any]:
        """Get the volume sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: self.device_attributes.dolby_mode,
        }

    def _get_surround_enhance_sensor_attributes(self) -> dict[str, Any]:
        """Get the surround-enhance sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: str(self.device_attributes.surround_enhance),
            SensorAttr.UNIT: "dB",
        }

    def _get_lfe_enhance_sensor_attributes(self) -> dict[str, Any]:
        """Get the LFE-enhance sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: str(self.device_attributes.lfe_enhance),
            SensorAttr.UNIT: "dB",
        }

    def _get_loudness_sensor_attributes(self) -> dict[str, Any]:
        """Get the loudness sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: self.device_attributes.loudness,
        }

    def _get_mute_sensor_attributes(self) -> dict[str, Any]:
        """Get the mute sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: "on" if self.device_attributes.muted else "off",
            SensorAttr.UNIT: "sound",
        }

    def _get_preset_sensor_attributes(self) -> dict[str, Any]:
        """Get the preset sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: self.device_attributes.preset,
        }

    def _get_source_sensor_attributes(self) -> dict[str, Any]:
        """Get the source sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: self.device_attributes.source,
        }

    def _get_storm_xt_sensor_attributes(self) -> dict[str, Any]:
        """Get the StormXT sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: "on" if self.device_attributes.storm_xt_active else "off",
            SensorAttr.UNIT: "sound",
        }

    def _get_treble_sensor_attributes(self) -> dict[str, Any]:
        """Get the treble sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: str(self.device_attributes.treble),
            SensorAttr.UNIT: "dB",
        }

    def _get_upmixer_mode_sensor_attributes(self) -> dict[str, Any]:
        """Get the volume sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: self.device_attributes.actual_sound_mode,
        }

    def _get_volume_sensor_attributes(self) -> dict[str, Any]:
        """Get the volume sensor attributes."""
        return {
            SensorAttr.STATE: SENSOR_STATE_MAPPING[self.state],
            SensorAttr.VALUE: str(self.device_attributes.volume - 100),
            SensorAttr.UNIT: "dB",
        }

    async def power_on(self):
        """Power on the StormAudio processor."""
        await self._send_command(StormAudioCommands.POWER_ON)
        await self._send_command(StormAudioCommands.PROC_STATE)
        await self._wait_for_response(StormAudioResponses.PROC_STATE_ON, MAX_TIME_OUT)

    async def power_off(self):
        """Power off the StormAudio processor."""
        await self._send_command(StormAudioCommands.POWER_OFF)
        await self._send_command(StormAudioCommands.PROC_STATE)
        await self._wait_for_response(StormAudioResponses.PROC_STATE_OFF)

    async def power_toggle(self):
        """Toggle the power of the StormAudio processor."""
        current_power_state = self.state

        await self._send_command(StormAudioCommands.POWER_TOGGLE)
        await self._send_command(StormAudioCommands.PROC_STATE)

        if current_power_state == StormAudioStates.ON:
            await self._wait_for_response(StormAudioResponses.PROC_STATE_OFF)
        else:
            await self._wait_for_response(
                StormAudioResponses.PROC_STATE_ON, MAX_TIME_OUT
            )

    async def mute_on(self):
        """Mute the StormAudio processor."""
        await self._send_command(StormAudioCommands.MUTE_ON)
        await self._wait_for_response(StormAudioResponses.MUTE_ON)

    async def mute_off(self):
        """Unmute the StormAudio processor."""
        await self._send_command(StormAudioCommands.MUTE_OFF)
        await self._wait_for_response(StormAudioResponses.MUTE_OFF)

    async def mute_toggle(self):
        """Toggle mute of the StormAudio processor."""
        await self._send_command(StormAudioCommands.MUTE_TOGGLE)

    async def volume_x(self, volume):
        """Set the volume of the StormAudio processor."""
        # The UC remotes only support absolute volume scales for now.
        # That's why we need to convert the relative values from the ISPs.
        sanitized_volume = max(MIN_VOLUME, min(MAX_VOLUME, int(volume)))
        relative_volume = sanitized_volume - MAX_VOLUME
        await self._send_command(
            StormAudioCommands.VOLUME_X_FORMAT.format(relative_volume)
        )
        await self._wait_for_response(
            pattern=StormAudioResponses.VOLUME_X,
            prefix_match=True,
        )

    async def volume_up(self):
        """Increase the volume of the StormAudio processor by 1dB."""
        await self._send_command(StormAudioCommands.VOLUME_UP)
        await self._wait_for_response(
            pattern=StormAudioResponses.VOLUME_X,
            prefix_match=True,
        )

    async def volume_down(self):
        """Decrease the volume of the StormAudio processor by 1dB."""
        await self._send_command(StormAudioCommands.VOLUME_DOWN)
        await self._wait_for_response(
            pattern=StormAudioResponses.VOLUME_X,
            prefix_match=True,
        )

    async def select_source(self, source: str):
        """Select the input of the StormAudio processor."""
        source_id = self.device_attributes.sources.get(source)

        if source_id is not None:
            await self._send_command(
                StormAudioCommands.INPUT_X_FORMAT.format(source_id)
            )
            await self._wait_for_response(
                StormAudioResponses.INPUT_X_FORMAT.format(source_id)
            )

    async def select_sound_mode(self, mode: str):
        """Set the surround mode of the StormAudio processor."""
        sound_mode_id = self.device_attributes.upmixer_modes.get(mode)

        if sound_mode_id is not None:
            await self._send_command(
                StormAudioCommands.SURROUND_MODE_X_FORMAT.format(sound_mode_id)
            )

    async def cursor_up(self):
        """Navigate up."""
        await self._send_command(StormAudioCommands.NAV_UP)
        await self._wait_for_response(StormAudioResponses.NAV_UP)

    async def cursor_down(self):
        """Navigate down."""
        await self._send_command(StormAudioCommands.NAV_DOWN)
        await self._wait_for_response(StormAudioResponses.NAV_DOWN)

    async def cursor_left(self):
        """Navigate left."""
        await self._send_command(StormAudioCommands.NAV_LEFT)
        await self._wait_for_response(StormAudioResponses.NAV_LEFT)

    async def cursor_right(self):
        """Navigate right."""
        await self._send_command(StormAudioCommands.NAV_RIGHT)
        await self._wait_for_response(StormAudioResponses.NAV_RIGHT)

    async def cursor_enter(self):
        """Enter the selected item."""
        await self._send_command(StormAudioCommands.NAV_OK)
        await self._wait_for_response(StormAudioResponses.NAV_OK)

    async def back(self):
        """Navigate back."""
        await self._send_command(StormAudioCommands.NAV_BACK)
        await self._wait_for_response(StormAudioResponses.NAV_BACK)

    # --- simple commands ---
    async def preset_next(self):
        """Set the next preset."""
        await self._send_command(StormAudioCommands.PRESET_NEXT)

    async def preset_prev(self):
        """Set the previous preset."""
        await self._send_command(StormAudioCommands.PRESET_PREV)

    async def loudness_off(self):
        """Set the loudness to off."""
        await self._send_command(StormAudioCommands.LOUDNESS_OFF)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_OFF)

    async def loudness_low(self):
        """Set the loudness to low."""
        await self._send_command(StormAudioCommands.LOUDNESS_LOW)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_LOW)

    async def loudness_medium(self):
        """Set the loudness to medium."""
        await self._send_command(StormAudioCommands.LOUDNESS_MEDIUM)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_MEDIUM)

    async def loudness_full(self):
        """Set the loudness to full."""
        await self._send_command(StormAudioCommands.LOUDNESS_FULL)
        await self._wait_for_response(StormAudioResponses.LOUDNESS_FULL)

    async def bass_up(self):
        """Increase the bass by 1dB."""
        await self._send_command(StormAudioCommands.BASS_UP)
        await self._wait_for_response(
            pattern=StormAudioResponses.BASS_X,
            prefix_match=True,
        )

    async def bass_down(self):
        """Decrease the bass by 1dB."""
        await self._send_command(StormAudioCommands.BASS_DOWN)
        await self._wait_for_response(
            pattern=StormAudioResponses.BASS_X,
            prefix_match=True,
        )

    async def bass_reset(self):
        """Reset the bass."""
        await self._send_command(StormAudioCommands.BASS_RESET)
        await self._wait_for_response(
            pattern=StormAudioResponses.BASS_X,
            prefix_match=True,
        )

    async def treble_up(self):
        """Increase the treble by 1dB."""
        await self._send_command(StormAudioCommands.TREBLE_UP)
        await self._wait_for_response(
            pattern=StormAudioResponses.TREBLE_X,
            prefix_match=True,
        )

    async def treble_down(self):
        """Decrease the treble by 1dB."""
        await self._send_command(StormAudioCommands.TREBLE_DOWN)
        await self._wait_for_response(
            pattern=StormAudioResponses.TREBLE_X,
            prefix_match=True,
        )

    async def treble_reset(self):
        """Reset the treble."""
        await self._send_command(StormAudioCommands.TREBLE_RESET)
        await self._wait_for_response(
            pattern=StormAudioResponses.TREBLE_X,
            prefix_match=True,
        )

    async def brightness_up(self):
        """Increase the brightness by 1dB."""
        await self._send_command(StormAudioCommands.BRIGHTNESS_UP)
        await self._wait_for_response(
            pattern=StormAudioResponses.BRIGHTNESS_X,
            prefix_match=True,
        )

    async def brightness_down(self):
        """Decrease the brightness by 1dB."""
        await self._send_command(StormAudioCommands.BRIGHTNESS_DOWN)
        await self._wait_for_response(
            pattern=StormAudioResponses.BRIGHTNESS_X,
            prefix_match=True,
        )

    async def brightness_reset(self):
        """Reset the brightness."""
        await self._send_command(StormAudioCommands.BRIGHTNESS_RESET)
        await self._wait_for_response(
            pattern=StormAudioResponses.BRIGHTNESS_X,
            prefix_match=True,
        )

    async def center_enhance_up(self):
        """Increase the center enhancement by 1dB."""
        await self._send_command(StormAudioCommands.CENTER_ENHANCE_UP)
        await self._wait_for_response(
            pattern=StormAudioResponses.CENTER_ENHANCE_X,
            prefix_match=True,
        )

    async def center_enhance_down(self):
        """Decrease the center enhancement by 1dB."""
        await self._send_command(StormAudioCommands.CENTER_ENHANCE_DOWN)
        await self._wait_for_response(
            pattern=StormAudioResponses.CENTER_ENHANCE_X,
            prefix_match=True,
        )

    async def center_enhance_reset(self):
        """Reset the center enhancement."""
        await self._send_command(StormAudioCommands.CENTER_ENHANCE_RESET)
        await self._wait_for_response(
            pattern=StormAudioResponses.CENTER_ENHANCE_X,
            prefix_match=True,
        )

    async def surround_enhance_up(self):
        """Increase the surround enhancement by 1dB."""
        await self._send_command(StormAudioCommands.SURROUND_ENHANCE_UP)
        await self._wait_for_response(
            pattern=StormAudioResponses.SURROUND_ENHANCE_X,
            prefix_match=True,
        )

    async def surround_enhance_down(self):
        """Decrease the surround enhancement by 1dB."""
        await self._send_command(StormAudioCommands.SURROUND_ENHANCE_DOWN)
        await self._wait_for_response(
            pattern=StormAudioResponses.SURROUND_ENHANCE_X,
            prefix_match=True,
        )

    async def surround_enhance_reset(self):
        """Reset the surround enhancement."""
        await self._send_command(StormAudioCommands.SURROUND_ENHANCE_RESET)
        await self._wait_for_response(
            pattern=StormAudioResponses.SURROUND_ENHANCE_X,
            prefix_match=True,
        )

    async def lfe_enhance_up(self):
        """Increase the LFE enhancement by 1dB."""
        await self._send_command(StormAudioCommands.LFE_ENHANCE_UP)
        await self._wait_for_response(
            pattern=StormAudioResponses.LFE_ENHANCE_X,
            prefix_match=True,
        )

    async def lfe_enhance_down(self):
        """Decrease the LFE enhancement by 1dB."""
        await self._send_command(StormAudioCommands.LFE_ENHANCE_DOWN)
        await self._wait_for_response(
            pattern=StormAudioResponses.LFE_ENHANCE_X,
            prefix_match=True,
        )

    async def lfe_enhance_reset(self):
        """Reset the LFE enhancement."""
        await self._send_command(StormAudioCommands.LFE_ENHANCE_RESET)
        await self._wait_for_response(
            pattern=StormAudioResponses.LFE_ENHANCE_X,
            prefix_match=True,
        )

    async def dolby_mode_off(self):
        """Set the Dolby mode to off mode."""
        await self._send_command(StormAudioCommands.DOLBY_MODE_OFF)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_OFF)

    async def dolby_mode_movie(self):
        """Set the Dolby mode to movie mode."""
        await self._send_command(StormAudioCommands.DOLBY_MODE_MOVIE)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_MOVIE)

    async def dolby_mode_music(self):
        """Set the Dolby mode to music mode."""
        await self._send_command(StormAudioCommands.DOLBY_MODE_MUSIC)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_MUSIC)

    async def dolby_mode_night(self):
        """Set the Dolby mode to night mode."""
        await self._send_command(StormAudioCommands.DOLBY_MODE_NIGHT)
        await self._wait_for_response(StormAudioResponses.DOLBY_MODE_NIGHT)

    async def storm_xt_on(self):
        """Set the StormXT mode to on."""
        await self._send_command(StormAudioCommands.STORM_XT_ON)

    async def storm_xt_off(self):
        """Set the StormXT mode to off."""
        await self._send_command(StormAudioCommands.STORM_XT_OFF)

    async def storm_xt_toggle(self):
        """Toggle the StormXT mode."""
        await self._send_command(StormAudioCommands.STORM_XT_TOGGLE)

    async def auro_preset_small(self):
        """Set the Auro-Matic preset to "small"."""
        await self._send_command(StormAudioCommands.AURO_PRESET_SMALL)

    async def auro_preset_medium(self):
        """Set the Auro-Matic preset to "medium"."""
        await self._send_command(StormAudioCommands.AURO_PRESET_MEDIUM)

    async def auro_preset_large(self):
        """Set the Auro-Matic preset to "large"."""
        await self._send_command(StormAudioCommands.AURO_PRESET_LARGE)

    async def auro_preset_speech(self):
        """Set the Auro-Matic preset to "speech"."""
        await self._send_command(StormAudioCommands.AURO_PRESET_SPEECH)

    async def auro_preset_x(self, auro_preset_name: str):
        """Set the Auro-Matic preset to the given value."""
        auro_preset_id = self.device_attributes.auro_presets.get(auro_preset_name)

        if auro_preset_id is not None:
            await self._send_command(
                StormAudioCommands.AURO_PRESET_X_FORMAT.format(auro_preset_id)
            )

    async def auro_strength_x(self, auro_strength: int):
        """Set the Auro-Matic strength to the given value."""
        if int(auro_strength) in self.device_attributes.auro_strength_list:
            await self._send_command(
                StormAudioCommands.AURO_STRENGTH_X_FORMAT.format(auro_strength)
            )
        else:
            _LOG.error(
                f"[%s] Invalid Auro-Matic strength: {auro_strength}", self.log_id
            )

    # --- Custom commands from the Remote entity ---
    async def preset_x(self, preset_name: str):
        """Select a preset by name."""
        preset_id = self.device_attributes.presets.get(preset_name)

        if preset_id is not None:
            await self._send_command(
                StormAudioCommands.PRESET_X_FORMAT.format(preset_id)
            )
            await self._wait_for_response(
                StormAudioResponses.PRESET_X_FORMAT.format(preset_id)
            )

    async def custom_command(self, command: str):
        """Send any of the ISP's supported Telnet commands to the device."""
        await self._send_command(command)
