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
