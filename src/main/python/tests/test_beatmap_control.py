from fbs_runtime.application_context import ApplicationContext
import unittest
from pathlib import Path
from nc2dt.core.osu_db import Beatmap
from nc2dt.core.beatmap_control import BeatmapControl
from nc2dt.utils import set_app_context
import shutil
from .utils import asset_path_builder
import os


class TestBeatmapControl(unittest.TestCase):
    def setUp(self):
        set_app_context(ApplicationContext())
        self.osu_path = asset_path_builder(Path("mock_osu_folder"))
        self.beatmap_folder = self.osu_path / Path("Songs/1")
        self.beatmap = Beatmap("Artist", "Title", "Creator", "Diff", "audio.mp3", "1")
        beep = self.beatmap_folder / Path("beep.mp3")
        shutil.copy(beep, self.beatmap_folder / Path("audio.mp3"))
    
    def tearDown(self):
        set_app_context(None)
        for f in self.beatmap_folder.glob("*"):
            if f.name != "beep.mp3":
                os.remove(str(f))

    def test_has_converted_version(self):
        beatmap_control = BeatmapControl(self.beatmap, self.osu_path)
        self.assertFalse(beatmap_control.has_converted_version)
        beatmap_control.create_converted_version()
        self.assertTrue(beatmap_control.has_converted_version)
    
    def test_active_version(self):
        beatmap_control = BeatmapControl(self.beatmap, self.osu_path)
        # We didn't even convert, so that should error.
        with self.assertRaises(RuntimeError):
            beatmap_control.active_version
        beatmap_control.create_converted_version()
        self.assertEqual(beatmap_control.active_version, "original")
        beatmap_control.switch_to_version("nc2dt")
        self.assertEqual(beatmap_control.active_version, "nc2dt")

