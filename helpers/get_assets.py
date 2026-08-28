"""Get Assets Folder helper"""
import sys
from pathlib import Path

def get_assets_route(relative_path: str) -> Path:
    """Returns de correct route of Assets folder whether is running from source code
    or as a PyInstaller executable.
    """
    if hasattr(sys,'_MEIPASS'):
        base_dir = Path(sys._MEIPASS)
    else:
        base_dir = Path(__file__).resolve().parent.parent
    return base_dir / relative_path

if __name__ == "__main__":
    print(get_assets_route("assets/json_language/hang_es.json"))
    print(get_assets_route("assets/images_core/hangman_0.png"))
    print(get_assets_route("assets/json_language/hang_fr.json"))
