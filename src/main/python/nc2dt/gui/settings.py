from nc2dt.core.osu_db import get_default_osu_path
from PyQt5.QtCore import QSettings
from pathlib import Path

def _get_settings():
    return QSettings("NC2DT", "ekisu")

def get_osu_path():
    settings = _get_settings()
    osu_path_str = settings.value("osu_path", type=str)
    if osu_path_str == "":
        return get_default_osu_path()
    return Path(osu_path_str)

def set_osu_path(path_str):
    settings = _get_settings()
    settings.setValue("osu_path", path_str)
