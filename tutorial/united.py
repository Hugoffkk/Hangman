"""United Tutorials screens"""
# [Global imports]
import sys

# PyQt5 imports
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget

# Language imports
from helpers.lang_config import LANGUAGE_CODE
from helpers.load_lang import load_language

# Imports from tutorial modules
from tutorial.goal import GoalScreen
from tutorial.rule1 import RuleOneScreen
from tutorial.rule2 import RuleTwoScreen
from tutorial.rule3 import RuleThreeScreen
from tutorial.rule4 import RuleFourScreen
from tutorial.rule5 import RuleFiveScreen
from tutorial.rule6 import RuleSixScreen
from tutorial.rule7 import RuleSevenScreen
from tutorial.rule8 import RuleEightScreen

from introduction.intro_screen import IntroScreen
from core.game_screen import TheHangmanScreen

class UnitedTutorialScreen(QWidget):
    def __init__(self):
        super().__init__()
        # [Loading language dict]
        self.language = load_language(LANGUAGE_CODE)

        # [Basic boilerplate]
        self.setWindowTitle(self.language["tutorial_title"])
        self.setGeometry(700,300,600,600)

        self.intro = IntroScreen()
        self.game = TheHangmanScreen()

        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Stacked Widget
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Screens list
        self.tutorial_screens = [
            GoalScreen(),
            RuleOneScreen(),
            RuleTwoScreen(),
            RuleThreeScreen(),
            RuleFourScreen(),
            RuleFiveScreen(),
            RuleSixScreen(),
            RuleSevenScreen(),
            RuleEightScreen(),
        ]

        # Add screens to stacked widget
        for screen in self.tutorial_screens:
            self.stacked_widget.addWidget(screen)
        self.setup_signals()

    def setup_signals(self):
        for screen in self.tutorial_screens:
            if hasattr(screen, 'go_next_screen'):
                screen.go_next_screen.connect(self.go_next)
            if hasattr(screen, 'go_previous_screen'):
                screen.go_previous_screen.connect(self.go_previous)
            if hasattr(screen, 'go_to_menu'):
                screen.go_to_menu.connect(self.go_menu)
            if hasattr(screen, 'go_to_game'):
                screen.go_to_game.connect(self.go_game)

    def go_next(self):
            current_index = self.stacked_widget.currentIndex()
            if current_index < self.stacked_widget.count() - 1:
                self.stacked_widget.setCurrentIndex(current_index + 1)

    def go_previous(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index > 0:
            self.stacked_widget.setCurrentIndex(current_index - 1)

    def go_menu(self):
        self.close()
        self.intro.show()

    def go_game(self):
        self.close()
        self.game.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UnitedTutorialScreen()
    window.show()
    sys.exit(app.exec_())

