# A better name for this file/class would come in handy.

from .osu_db import Beatmap
from .audio import Audio
from nc2dt.utils import debug
from pathlib import Path
import time

class BeatmapControl(object):
    def __init__(self, beatmap: Beatmap, osu_path: Path):
        self.osu_path = osu_path
        self.beatmap = beatmap


    @property
    def absolute_folder(self) -> Path:
        return self.osu_path / Path("Songs") / Path(self.beatmap.folder_name)
    
    @property
    def beatmap_audio_path(self):
        return self.absolute_folder / Path(self.beatmap.audio)

    @property
    def nc2dt_audio_path(self):
        return self.absolute_folder / Path(self.beatmap.audio + ".nc2dt")
    
    @property
    def nc2dt_original_audio_path(self):
        return self.absolute_folder / Path(self.beatmap.audio + ".nc2dt-orig")

    @property
    def has_converted_version(self):
        # Either we have a audio with the .nc2dt extension,
        # or one with the .nc2dt-orig extension, representing that the
        # nc2dt version is the one with the "normal" filename.
        return self.nc2dt_audio_path.exists() or self.nc2dt_original_audio_path.exists()
    
    @property
    def active_version(self):
        if not self.has_converted_version:
            raise RuntimeError("There's no converted version to begin with!")
        
        # If the converted version path exists, it means we're currently using
        # the original one, and vice-versa.
        if self.nc2dt_audio_path.exists():
            return "original"
        else:
            return "nc2dt"

    def create_converted_version(self):
        debug("BeatmapControl.create_converted_version: started.")
        start = time.process_time()
        audio = Audio(self.beatmap_audio_path)
        end = time.process_time()
        debug("BeatmapControl.create_converted_version: read file in ", end - start, "seconds")

        start = time.process_time()
        audio.convert_nc_to_dt()
        end = time.process_time()
        debug("BeatmapControl.create_converted_version: NC2DT in ", end - start, "seconds")
        
        start = time.process_time()
        audio.export(self.nc2dt_audio_path)
        end = time.process_time()
        debug("BeatmapControl.create_converted_version: exported in ", end - start, "seconds")
    
    def switch_to_version(self, version):
        if not self.has_converted_version:
            raise RuntimeError("There's no converted version to begin with!")
        
        if version == self.active_version:
            return
        
        if version == "nc2dt":
            self.beatmap_audio_path.rename(self.nc2dt_original_audio_path)
            self.nc2dt_audio_path.rename(self.beatmap_audio_path)
        elif version == "original":
            self.beatmap_audio_path.rename(self.nc2dt_audio_path)
            self.nc2dt_original_audio_path.rename(self.beatmap_audio_path)
