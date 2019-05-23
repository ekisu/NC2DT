import os.path
from pathlib import Path

def log(*args, **kwargs):
    print("LOG: ", *args, **kwargs)


def debug(*args, **kwargs):
    print("DEBUG: ", *args, **kwargs)

ROOT_PATH = Path(__file__).parent.parent.absolute()

def resource_path(path: Path) -> Path:
    return ROOT_PATH / Path("resources") / path
