from fbs_runtime.application_context import ApplicationContext
from nc2dt.gui.main_window import MainWindow
from nc2dt.core.osu_db import OsuDB, get_default_osu_path
from nc2dt.utils import set_app_context
from pathlib import Path
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    osu_path = get_default_osu_path()
    osu_db_file_path = osu_path / Path("osu!.db")
    osu_db = OsuDB(osu_db_file_path)

    appctxt = ApplicationContext()
    set_app_context(appctxt)
    main_window = MainWindow(osu_db)
    main_window.show()
    sys.exit(appctxt.app.exec())
