"""Get language package helper"""
import json
from . import get_assets

def load_language(code: str) -> dict[str,str]:
    """Gets language dict from its proper json"""
    route = get_assets.get_assets_route(f"assets/json_language/hang_{code}.json")
    with open(route,"r",encoding='utf-8') as f:
        language = json.load(f)

    return language

if __name__ == "__main__":
    language = load_language("fr")
    print(language["title"])