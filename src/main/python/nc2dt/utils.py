import os.path
from pathlib import Path

def log(*args, **kwargs):
    print("LOG: ", *args, **kwargs)


def debug(*args, **kwargs):
    print("DEBUG: ", *args, **kwargs)

_APP_CONTEXT = None
def set_app_context(app_context):
    global _APP_CONTEXT
    _APP_CONTEXT = app_context

def resource_path(path: Path) -> Path:
    global _APP_CONTEXT
    if _APP_CONTEXT is None:
        raise RuntimeError("AppContext not set!")
    
    return Path(_APP_CONTEXT.get_resource(str(path)))

def get_sox_executable():
    return str(resource_path(Path("sox/sox.exe")))

def get_soundstretch_executable():
    return str(resource_path(Path("soundstretch.exe")))
