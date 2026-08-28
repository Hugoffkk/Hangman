"""Hangman Screen Game"""

import sys
import qdarktheme
from .game import TheHangmanGame
from .style_game import DARK_THEME, LIGHT_THEME
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)
from helpers.lang_config import LANGUAGE_CODE
from helpers.load_lang import load_language
from helpers.get_assets import get_assets_route


class TheHangmanScreen(QWidget):
    def __init__(self):
        super().__init__()

        # [Loading language dict]
        self.language = load_language(LANGUAGE_CODE)

        # [Creating game]
        self.game = TheHangmanGame()

        # [Basic game boilerplate]
        self.setWindowTitle(self.language["title"])
        self.setGeometry(700, 300, 600, 600)

        self.word = self.game.request_word()

        # Guardar referencias de las ventanas secundarias para evitar garbage collection
        self.win_screen = None
        self.defeat_screen = None

        # [Layout]
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)

        # [Title]
        self.title = QLabel(self.language["help"])

        # [Hangman Image]
        self.image = QLabel()
        self.pixmap = QPixmap(str(get_assets_route("assets/images_core/hangman_0.png")))
        self.image.setPixmap(self.pixmap)

        # [Word hints]
        self.undercores = QLabel(self.game.word_status)

        # [Input entry]
        self.input = QLineEdit()
        self.input.setPlaceholderText(self.language["user_input"])

        # [Buttons]
        self.setStyleSheet(LIGHT_THEME)

        self.toggle_button = QPushButton(self.language["light_theme"])
        self.toggle_button.setCheckable(True)

        self.TPause_layout = QHBoxLayout()
        self.TPause_layout.addStretch(1)
        self.TPause_layout.addWidget(self.toggle_button, alignment=Qt.AlignmentFlag.AlignRight)
        self.main_layout.addLayout(self.TPause_layout)

        self.toggle_button.toggled.connect(self.on_toggle_change)

        self.try_button = QPushButton("↪")
        self.try_button.setFixedHeight(26)
        self.try_button.setFixedWidth(26)

        self.surrender_button = QPushButton("🏳️")
        self.surrender_button.setFixedHeight(26)
        self.surrender_button.setFixedWidth(26)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.buttons_layout.addWidget(self.try_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.buttons_layout.addWidget(self.surrender_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.buttons_layout.addStretch()

        for btn in (self.toggle_button, self.surrender_button, self.try_button):
            btn.setCursor(Qt.PointingHandCursor)

        # [Incorrect letters/words]
        wrong_text = " - ".join(self.game.incorrect_guess)
        self.incorrect = QLabel(f"{self.language['wrong_letters']} {wrong_text}")

        # [Lives]
        self.lives = QLabel(f"{self.language['lives']}" + "❤" * self.game.lives)

        # [Add to layout]
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.image, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.undercores, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.incorrect, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.lives, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addStretch()

        # [StyleSheet Names]
        self.title.setObjectName("title")
        self.undercores.setObjectName("undercores")
        self.incorrect.setObjectName("incorrect")
        self.lives.setObjectName("lives")
        self.toggle_button.setObjectName("toggle_button")
        self.input.setObjectName("input")
        self.try_button.setObjectName("try_button")
        self.surrender_button.setObjectName("surrender_button")

        # [Connecting buttons]
        self.try_button.clicked.connect(self.try_input)
        self.surrender_button.clicked.connect(self.surrender)
        self.input.returnPressed.connect(self.try_input)

    def on_toggle_change(self, checked):
        if checked:
            self.toggle_button.setText(self.language["dark_theme"])
            self.setStyleSheet(DARK_THEME)
        else:
            self.toggle_button.setText(self.language["light_theme"])
            self.setStyleSheet(LIGHT_THEME)

    def update_ui(self):
        self.undercores.setText(self.game.word_status)
        wrong_text = " - ".join(self.game.incorrect_guess)
        self.incorrect.setText(f"{self.language['wrong_letters']} {wrong_text}")
        self.lives.setText(f"{self.language['lives']}" + "❤" * self.game.lives)

        stage = 6 - self.game.lives
        image_path = str(get_assets_route(f"assets/images_core/hangman_{stage}.png"))
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.image.setPixmap(pixmap)

    def animate_shake_input(self):
        original_pos = self.input.pos()
        self.shake_anim = QPropertyAnimation(self.input, b"pos")
        self.shake_anim.setDuration(250)
        self.shake_anim.setKeyValueAt(0.0, original_pos)
        self.shake_anim.setKeyValueAt(0.2, original_pos + QPoint(-8, 0))
        self.shake_anim.setKeyValueAt(0.4, original_pos + QPoint(8, 0))
        self.shake_anim.setKeyValueAt(0.6, original_pos + QPoint(-5, 0))
        self.shake_anim.setKeyValueAt(0.8, original_pos + QPoint(5, 0))
        self.shake_anim.setKeyValueAt(1.0, original_pos)
        self.shake_anim.start()

    def try_input(self):
        """Input method"""
        from core.win_screen import WinScreen
        from core.defeat_screen import DefeatScreen

        guess = self.input.text()
        result = self.game.try_guess(guess)

        if result == "won":
            self.win_screen = WinScreen()
            self.win_screen.show()
            self.close()
        elif result == "defeated":
            self.defeat_screen = DefeatScreen(self.word)
            self.defeat_screen.show()
            self.close()
        elif result == "invalid" or result == "repeated":
            self.animate_shake_input()
        else:
            self.input.clear()
            self.update_ui()

    def surrender(self):
        """Surrender method"""
        from core.defeat_screen import DefeatScreen
        self.defeat_screen = DefeatScreen(self.word)
        self.defeat_screen.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TheHangmanScreen()
    window.show()
    sys.exit(app.exec_())