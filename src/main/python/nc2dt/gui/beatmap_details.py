from .generated.beatmap_details import Ui_BeatmapDetails
from PyQt5 import QtWidgets
from nc2dt.core.osu_db import Beatmap
from nc2dt.core.beatmap_control import BeatmapControl
from .settings import get_osu_path
from nc2dt.utils import debug
from threading import Thread

class BeatmapDetails(QtWidgets.QDialog):
    def __init__(self, parent, beatmap: Beatmap):
        super().__init__(parent)
        self.beatmap = beatmap
        self.beatmapControl = BeatmapControl(self.beatmap, get_osu_path())
        self.ui = Ui_BeatmapDetails()
        self.ui.setupUi(self)
        self.updateUi()
        self.ui.switchAudioButton.clicked.connect(self.onSwitchAudioClicked)
        self.ui.createConvertedAudioButton.clicked.connect(self.onCreateConvertedAudioClicked)
    
    def updateUi(self):
        self.ui.artistLabel.setText(self.beatmap.artist)
        self.ui.titleLabel.setText(self.beatmap.title)
        self.ui.creatorLabel.setText(self.beatmap.creator)
        self.ui.difficultyLabel.setText(self.beatmap.difficulty)
        self.ui.audioLabel.setText(self.beatmap.audio)

        self.ui.createConvertedAudioButton.setEnabled(not self.beatmapControl.has_converted_version)
        self.ui.switchAudioButton.setEnabled(self.beatmapControl.has_converted_version)
        if self.beatmapControl.has_converted_version:
            if self.beatmapControl.active_version == "nc2dt":
                self.ui.switchAudioButton.setText("Switch to Original Audio")
            else:
                self.ui.switchAudioButton.setText("Switch to NC2DT Audio")
    
    def onSwitchAudioClicked(self):
        try:
            if self.beatmapControl.active_version == "nc2dt":
                self.beatmapControl.switch_to_version("original")
            else:
                self.beatmapControl.switch_to_version("nc2dt")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "NC2DT", (
                "Couldn't switch the audio. Maybe the song is opened/playing in osu!?\n"
                "Try selecting a different song in osu! and try again."
            ))
        
        self.updateUi()

    def onCreateConvertedAudioClicked(self):
        # This will block... Find a way to smoothly do this, unblocking.
        progress_dialog = QtWidgets.QProgressDialog("Converting...", None, 0, 0, self)
        progress_dialog.setWindowTitle("Conversion in progress...")

        def run_conversion():
            debug("Starting conversion...")
            self.beatmapControl.create_converted_version()
            debug("Closing progress dialog...")
            progress_dialog.close()
        
        t = Thread(target=run_conversion)
        t.start()
        progress_dialog.exec()
        debug("Past progress dialog...")
        t.join()
        self.updateUi()
