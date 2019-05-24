from fbs_runtime.application_context import ApplicationContext
from nc2dt.gui.main_window import MainWindow
from nc2dt.gui.settings import get_osu_path, set_osu_path
from nc2dt.core.osu_db import OsuDB, get_default_osu_path
from nc2dt.utils import set_app_context
from pathlib import Path
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    appctxt = ApplicationContext()
    set_app_context(appctxt)

    osu_path = get_default_osu_path()
    settings_osu_path = get_osu_path()
    if settings_osu_path is not None:
        osu_path = settings_osu_path
    osu_db_file_path = osu_path / Path("osu!.db")

    if not osu_db_file_path.exists():
        QtWidgets.QMessageBox.warning(None, "NC2DT", (
            "Couldn't find your osu! installation.\n"
            "Please select the folder where it's installed."
        ))
        new_path = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "Please select your osu! installation"
        )
        if new_path == "":
            QtWidgets.QMessageBox.critical(None, "NC2DT", "No folder was selected, exiting.")
            sys.exit(1)
        
        set_osu_path(new_path)
        osu_db_file_path = Path(new_path) / Path("osu!.db")

    try:
        osu_db = OsuDB(osu_db_file_path)
    except FileNotFoundError:
        QtWidgets.QMessageBox.critical(None, "NC2DT", "Couldn't open osu!.db. Exiting.")
        sys.exit(1)

    main_window = MainWindow(osu_db)
    main_window.show()
    sys.exit(appctxt.app.exec())
