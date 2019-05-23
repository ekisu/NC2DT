from pathlib import Path
from nc2dt.utils import debug, get_sox_executable, get_soundstretch_executable
import time
import ffmpeg
import os
from tempfile import NamedTemporaryFile
import subprocess

class Audio(object):
    def __init__(self, path: Path):
        self.path: Path = path
    
    def convert_nc_to_dt(self, out_path: Path):
        # Slow it to 2/3 of the original speed, altering the pitch, and
        # then speed it back up by 3/2, keeping the pitch.
        temp_decoded_file = NamedTemporaryFile(delete=False)
        temp_decoded_file.close()

        subprocess.run([
            get_sox_executable(),
            str(self.path),
            "-t", "wav",
            temp_decoded_file.name
        ])
        
        temp_soundstretch_output = NamedTemporaryFile(delete=False)
        temp_soundstretch_output.close()
        subprocess.run([
            get_soundstretch_executable(),
            temp_decoded_file.name,
            temp_soundstretch_output.name,
            "-rate=-33.3333%",
            "-tempo=50%"
        ])

        os.remove(temp_decoded_file.name)

        subprocess.run([
            get_sox_executable(),
            temp_soundstretch_output.name,
            "-t", "mp3",
            "-C", "192",
            str(out_path)
        ])

        os.remove(temp_soundstretch_output.name)