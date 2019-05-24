from fbs_runtime.application_context import ApplicationContext
import unittest
from nc2dt.core.audio import Audio
from nc2dt.utils import set_app_context
from pathlib import Path
from subprocess import CalledProcessError

def asset_path_builder(sub_path: Path) -> Path:
    assets_folder = Path(__file__).parent
    return assets_folder.joinpath(Path("assets"), sub_path)


class TestAudio(unittest.TestCase):
    def setUp(self):
        set_app_context(ApplicationContext())
    
    def tearDown(self):
        set_app_context(None)
    
    def test_non_existant_input_audio(self):
        path = asset_path_builder(Path("non_existant.mp3"))
        with self.assertRaises(FileNotFoundError):
            audio = Audio(path)
    
    def test_invalid_audio(self):
        path = asset_path_builder(Path("image.png"))
        with self.assertRaises(CalledProcessError):
            audio = Audio(path)
            audio.convert_nc_to_dt(asset_path_builder(Path("output.mp3")))


