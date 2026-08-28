"""Hangman game module"""

# Loading python's modules & local ones
import random,json
from helpers.get_assets import get_assets_route
from helpers import lang_config
from .utils import hidden_word,normalize_text

class TheHangmanGame():
    """Game class"""
    def __init__(self):
        # Gets words dict
        words_route = get_assets_route(f"assets/json_words/words_{lang_config.LANGUAGE_CODE}.json")
        with open(words_route,"r",encoding='utf-8') as f:
            self.words_list: list[str] = json.load(f)

        # Select a random word
        self.word = random.choice(self.words_list)

        # Game initial state
        self.lives: int = 6
        self.correct_letters: list[str] = []
        self.incorrect_guess: list[str] = []

    def __str__(self):
        return f"Wanted word: {self.word}  ||  Lives remaining: {self.lives}  ||  Status: {self.word_status}"

    @property
    def word_status(self) -> str:
        """Return the updated status of the word"""
        return hidden_word(self.word, self.correct_letters)

    def try_guess(self,raw_guess: str) -> str:
        """Game's logic"""

        # Verify the guess is valid and clean it
        if not raw_guess.isalpha():
            return "invalid"
        clean_guess = normalize_text(raw_guess.lower().strip())
        clean_word = normalize_text(self.word)

        # If the guess is the correct word or the word is completed
        if clean_guess == clean_word:
            return "won"

        # If the letter or word is repeated
        if clean_guess in self.correct_letters or clean_guess in self.incorrect_guess:
            return "repeated"

        # If the guess is a correct letter
        elif len(clean_guess) == 1 and clean_guess in clean_word:
            self.correct_letters.append(clean_guess)
            if self.is_won():
                return "won"
            return "correct"

        # If the guess is a incorrect letter/word
        elif len(clean_guess) >= 1 and clean_guess not in clean_word:
            self.lives -= 1
            self.incorrect_guess.append(clean_guess)
            if self.is_defeated():
                return "defeated"
            return "incorrect"
    
    def is_won(self) -> bool:
        """Verify if the word was revealed"""
        return self.word_status == self.word

    def is_defeated(self) -> bool:
        """Verify if the player has ran out of lives"""
        return self.lives <= 0

    def request_word(self):
        return self.word

    def reset(self) -> None:
        """Reset the game to not create more clases for new games"""
        # Select a random word
        self.word = random.choice(self.words_list)

        # Set initial state
        self.lives: int = 6
        self.correct_letters.clear()
        self.incorrect_guess.clear()


if __name__ == "__main__":
    # Testing
    game = TheHangmanGame()
    print(game)

    (game.try_guess("hesitation"))
    (game.try_guess("h"))
    (game.try_guess("a"))

    print(game)

    (game.try_guess("c"))
    print(game.try_guess("t"))
    print(game.try_guess("x"))
    print(game.try_guess("d"))


    print(game)

    game.reset()

    print(game)