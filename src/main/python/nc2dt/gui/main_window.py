from .generated.main_window import Ui_MainWindow
from .beatmap_details import BeatmapDetails
from PyQt5 import QtWidgets, QtGui
from nc2dt.core.osu_db import OsuDB
from nc2dt.utils import debug, resource_path
from .settings import set_osu_path, get_osu_path
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, osu_db: OsuDB):
        super().__init__()
        self.osu_db = osu_db
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        debug("Loading icon from", str(resource_path(Path("icon/nc2dt.png"))))
        self.setWindowIcon(QtGui.QIcon(str(resource_path(Path("icon/nc2dt.png")))))
        self.ui.beatmapSearchLineEdit.returnPressed.connect(self.onBeatmapSearchEnter)
        self.ui.beatmapsListView.doubleClicked.connect(self.onBeatmapResultDoubleClick)
        self.ui.actionChangeOsuPath.triggered.connect(self.onChangeOsuPath)
        self.itemModel = QtGui.QStandardItemModel(self.ui.beatmapsListView)
        self.ui.beatmapsListView.setModel(self.itemModel)

    def onBeatmapSearchEnter(self):
        search_term = self.ui.beatmapSearchLineEdit.text()
        debug("MainWindow: searching for ", search_term)
        results = self.osu_db.search_beatmap(search_term)
        debug("MainWindow: found {} results".format(len(results)))

        self.itemModel.clear()
        for beatmap in results:
            item = QtGui.QStandardItem("{} - {} ({}) [{}]".format(beatmap.artist, beatmap.title, beatmap.creator, beatmap.difficulty))
            item.setData(beatmap)
            self.itemModel.appendRow(item)
    
    def onBeatmapResultDoubleClick(self, index):
        item = self.itemModel.itemFromIndex(index)
        beatmap = item.data()
        debug("MainWindow.onBeatmapResultDoubleClick: got", beatmap)
        BeatmapDetails(self, beatmap).exec()
    
    def _reload_osu_db(self, osu_path):
        load_dialog = QtWidgets.QProgressDialog("Loading osu!.db...", None, 0, 0, self)
        load_dialog.setWindowTitle("Reload in progress...")

        def do_reload():
            try:
                new_osu_db = OsuDB(osu_path / Path("osu!.db"))
                self.osu_db = new_osu_db
            except FileNotFoundError:
                load_dialog.close()
                return False
            load_dialog.close()
            return True
        
        executor = ThreadPoolExecutor()
        task = executor.submit(do_reload)
        load_dialog.exec()

        if not task.result():
            QtWidgets.QMessageBox.critical(None, "NC2DT", "Couldn't open osu!.db. Exiting.")
            load_dialog.close()
            self.close()

    def onChangeOsuPath(self):
        new_path = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "Please select your osu! installation"
        )
        if new_path == "":
            return
        
        set_osu_path(new_path)
        self._reload_osu_db(get_osu_path()) 

