"""
Device attributes for the Integration.

:license: Mozilla Public License Version 2.0, see LICENSE for more details.
"""

from dataclasses import dataclass, field

from uc_intg_stormaudio.const import StormAudioStates


@dataclass
class StormAudioDeviceAttributes:
    """
    Device attributes dataclass.

    This dataclass holds all the current state of our StormAudio ISP.
    """

    auro_preset_id: int | None = None
    auro_presets: dict[str, int] = field(
        default_factory=lambda: {
            "Small": 0,
            "Medium": 1,
            "Large": 2,
            "Speech": 3,
        }
    )
    auro_strength: int | None = None
    auro_strength_list: list[int] = field(default_factory=lambda: list(range(0, 15)))
    bass: int = 0
    brightness: int = 0
    center_enhance: int = 0
    dolby_mode_id: int | None = None
    dolby_modes: dict[int, str] = field(
        default_factory=lambda: {
            0: "Off",
            1: "Movie",
            2: "Music",
            3: "Night",
        }
    )
    lfe_enhance: int = 0
    loudness_mode_id: int | None = None
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
    surround_enhance: int = 0
    treble: int = 0
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
    actual_upmixer_mode_id: int | None = None
    volume: int = 0

    @property
    def auro_preset(self) -> str | None:
        """Returns the current Auro-Matic preset."""
        try:
            return list(self.auro_presets.keys())[
                list(self.auro_presets.values()).index(self.auro_preset_id)
            ]
        except ValueError:
            return None

    @property
    def auro_preset_list(self) -> list[str]:
        """Returns a list of the Auro-Matic presets."""
        return list(self.auro_presets.keys())

    @property
    def dolby_mode(self) -> str:
        """Returns the current dolby mode setting."""
        return self.dolby_modes.get(self.dolby_mode_id)

    @property
    def loudness(self) -> str:
        """Returns the current loudness setting."""
        return self.loudness_modes.get(self.loudness_mode_id)

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
    def preset_list(self) -> list[str]:
        """Returns a list of the available presets."""
        return list(self.presets.keys())

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
    def actual_sound_mode(self) -> str | None:
        """Returns the current actual sound mode."""
        try:
            return list(self.upmixer_modes.keys())[
                list(self.upmixer_modes.values()).index(self.actual_upmixer_mode_id)
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
