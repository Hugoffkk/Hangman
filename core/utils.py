"""Utilities' module for the game class"""
import unicodedata

def hidden_word(word: str, guessed_letters: list[str]) -> str:
    """Returns the status of the word"""
    return "".join(x if x in guessed_letters else " _" for x in word)

def normalize_text(text: str) -> str:
    """Normalize words with characters like 'é','à','ê' or 'ç' in other languages"""
    nfkd = unicodedata.normalize('NFKD', text)
    return "".join([c for c in nfkd if not unicodedata.combining(c)])


if __name__ == "__main__":
    # Testing

    # Testing hidden words function
    assert hidden_word("cat", ["c", "t"]) == "c _t", "It shoud hide the letter 'a'"
    assert hidden_word("dog", []) == " _ _ _", "Without letters should show underscores"

    # Testing text normalizer function
    assert normalize_text("café") == "cafe"
    assert normalize_text("français") == "francais"
    assert normalize_text("árbol") == "arbol"

    # Result
    print("Module exectuded successfully")
