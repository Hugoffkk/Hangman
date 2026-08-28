"""Win screen module"""

import sys
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, 
    QPushButton, QVBoxLayout, QHBoxLayout
)
from helpers.lang_config import LANGUAGE_CODE
from helpers.load_lang import load_language
from helpers.get_assets import get_assets_route
from introduction.intro_screen import IntroScreen
from core.game_screen import TheHangmanScreen

class WinScreen(QWidget):
    def __init__(self):
        super().__init__()
        # [Loading language dict]
        self.language = load_language(LANGUAGE_CODE)

        # [Basic game boilerplate]
        self.setWindowTitle(self.language["title"])
        self.setGeometry(700, 300, 600, 600)

        # [Screens]
        self.intro_screen = IntroScreen()
        self.game_screen = TheHangmanScreen()

        # [Title]
        self.title = QLabel(f"{self.language['win']}")
        self.title.setObjectName("defeatTitle")
        self.title.setWordWrap(False)

        # [Images]
        self.image = QLabel()
        self.pixmap = QPixmap(str(get_assets_route("assets/AdobeCrown_hangman.png"))).scaled(350, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image.setPixmap(self.pixmap)

        # [Buttons]
        self.new_game = QPushButton(self.language["reset"])
        self.new_game.setObjectName("primaryButton")

        self.menu = QPushButton(self.language["menu"])
        self.menu.setObjectName("secondaryButton")

        for btn in (self.menu,self.new_game):
            btn.setFixedHeight(40)
            btn.setFixedWidth(80)

        self.new_game.clicked.connect(self.new_game_func)
        self.menu.clicked.connect(self.go_to_menu_func)

        # [Layout structure]
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(20)
        self.setLayout(self.main_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(15)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.new_game)
        self.buttons_layout.addWidget(self.menu)
        self.buttons_layout.addStretch()

        self.main_layout.addStretch()
        self.main_layout.addWidget(self.title,alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.image,alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addStretch()

        # [Apply custom QSS styling]
        self.apply_styles()

    def apply_styles(self):
        # [QSS stylesheet matching theme aesthetic]
        qss = """
            /* Defeat title styling */
            #defeatTitle {
                font-size: 26px;
                font-weight: bold;
                color: #000000;
                padding: 10px;
            }

            /* Generic button base styles */
            QPushButton {
                font-size: 14px;
                font-weight: 600;
                border-radius: 8px;
                padding: 10px 20px;
                min-width: 120px;
            }

            /* Primary action button (Reset/Retry) */
            #primaryButton {
                background-color: #11a4ff;
                color: #ffffff;
                border: none;
            }
            #primaryButton:hover {
                background-color: #0e8bd9;
            }
            #primaryButton:pressed {
                background-color: #0c74b4;
            }

            /* Secondary action button (Menu) */
            #secondaryButton {
                background-color: #11a4ff;
                color: #ffffff;
            }
            #secondaryButton:hover {
                background-color: #0e8bd9;
                color: #ffffff;
            }
            #secondaryButton:pressed {
                background-color: #0c74b4;
            }
        """
        self.setStyleSheet(qss)

    def new_game_func(self):
        self.close()
        self.game_screen.show()

    def go_to_menu_func(self):
        self.close()
        self.intro_screen.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WinScreen()
    window.show()
    sys.exit(app.exec_())