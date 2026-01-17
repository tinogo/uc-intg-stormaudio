"""
Device state for the Integration.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from uc_intg_stormaudio.const import StormAudioStates


@dataclass
class StormAudioDeviceState:
    """
    Device state dataclass.

    This dataclass holds all the current state of our StormAudio ISP.
    """

    loudness_mode: int | None = None
    loudness_modes: dict[int, str] = field(
        default_factory=lambda: {
            0: "Off",
            1: "Low",
            2: "Medium",
            3: "Full",
        }
    )
    muted: bool = False
    presets: dict[str, int] = field(default_factory=dict)
    preset_id: int | None = None
    sources: dict[str, int] = field(default_factory=dict)
    source_id: int | None = None
    state: StormAudioStates = StormAudioStates.UNKNOWN
    storm_xt_active: bool = False
    upmixer_modes: dict[str, int] = field(
        default_factory=lambda: {
            "Native": 0,
            "Stereo Downmix": 1,
            "Dolby Surround": 2,
            "DTS Neural:X": 3,
            "Auro-Matic": 4,
        }
    )
    upmixer_mode_id: int | None = None
    volume: int = 0

    # Naive change detection
    loudness_changed: bool = False
    muted_changed: bool = False
    presets_changed: bool = False
    preset_id_changed: bool = False
    sources_changed: bool = False
    source_id_changed: bool = False
    state_changed: bool = False
    storm_xt_active_changed: bool = False
    upmixer_mode_id_changed: bool = False
    volume_changed: bool = False

    @property
    def loudness(self) -> str:
        """Returns the current loudness setting."""
        return self.loudness_modes.get(self.loudness_mode)

    @property
    def preset(self) -> str | None:
        """Returns the current preset."""
        try:
            return list(self.presets.keys())[
                list(self.presets.values()).index(self.preset_id)
            ]
        except ValueError:
            return None

    @property
    def sound_mode_list(self) -> list[str]:
        """Returns a list of the available sound modes."""
        return list(self.upmixer_modes.keys())

    @property
    def sound_mode(self) -> str | None:
        """Returns the current sound mode."""
        try:
            return list(self.upmixer_modes.keys())[
                list(self.upmixer_modes.values()).index(self.upmixer_mode_id)
            ]
        except ValueError:
            return None

    @property
    def source_list(self) -> list[str]:
        """Returns a list of the available input sources."""
        return list(self.sources.keys())

    @property
    def source(self) -> str | None:
        """Returns the current source."""
        try:
            return list(self.sources.keys())[
                list(self.sources.values()).index(self.source_id)
            ]
        except ValueError:
            return None

    def reset_change_detection(self) -> None:
        """Reset the change detection flags."""
        self.loudness_changed = False
        self.muted_changed = False
        self.presets_changed = False
        self.preset_id_changed = False
        self.sources_changed = False
        self.source_id_changed = False
        self.state_changed = False
        self.storm_xt_active_changed = False
        self.upmixer_mode_id_changed = False
        self.volume_changed = False
