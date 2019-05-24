from pathlib import Path

def asset_path_builder(sub_path: Path) -> Path:
    assets_folder = Path(__file__).parent
    return assets_folder.joinpath(Path("assets"), sub_path)
