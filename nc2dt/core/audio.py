from pydub import AudioSegment
import pydub.effects
from pathlib import Path
from nc2dt.utils import debug
import time
import ffmpeg

class Audio(object):
    def __init__(self, path: Path):
        self.path: Path = path
        self.segment: AudioSegment = AudioSegment.from_file(path)
    
    def convert_nc_to_dt(self):
        # Slow it to 2/3 of the original speed, altering the pitch, and
        # then speed it back up by 3/2, keeping the pitch.
        frame_rate = self.segment.frame_rate
        new_frame_rate = int(frame_rate * 2/3)

        debug("Audio.convert_nc_to_dt: called.")
        start = time.process_time()
        slowed_down_segment = self.segment._spawn(
            self.segment.raw_data,
            overrides={'frame_rate': new_frame_rate}
        )
        end = time.process_time()
        debug("Audio.convert_nc_to_dt: created slowed segment in ", end - start, "seconds")
        # Not sure if this step is needed.
        start = time.process_time()
        resampled_slowed_down_segment = slowed_down_segment.set_frame_rate(44100)
        end = time.process_time()
        debug("Audio.convert_nc_to_dt: resampled in ", end - start, "seconds")

        start = time.process_time()
        self.segment = resampled_slowed_down_segment.speedup(frame_rate / new_frame_rate)
        end = time.process_time()
        debug("Audio.convert_nc_to_dt: speedup in ", end - start, "seconds")

    def export(self, *args, **kwargs):
        self.segment.export(*args, **kwargs)
