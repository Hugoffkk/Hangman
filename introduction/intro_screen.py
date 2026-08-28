"""Main Screen Game"""

import sys,qdarktheme
from PyQt5.QtCore import Qt,QPropertyAnimation, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout)
from helpers import lang_config
from helpers.load_lang import load_language
from helpers.get_assets import get_assets_route
from language.language_screen import LanguageScreen
from core.game_screen import TheHangmanScreen


class IntroScreen(QWidget):
    def __init__(self):
        super().__init__()
        # [Loading language dict]
        self.language = load_language(lang_config.LANGUAGE_CODE)

        # [Basic game boilerplate]
        self.setWindowTitle(self.language["title"])
        self.setGeometry(700,300,600,600)

        # [Layout]

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)

        # [Title]
        self.title = QLabel(self.language["intro"])

        # [Image]
        self.image = QLabel()
        self.pixmap = QPixmap(str(get_assets_route("assets/hangman_intro.png"))).scaled(350, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image.setPixmap(self.pixmap)

        # [Menu]
        self.tutorial = QPushButton(self.language["tutorial"])
        self.play = QPushButton(self.language["play"])

        for btn in (self.play,self.tutorial):
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedHeight(40)
            btn.setFixedWidth(120)

        # [Adding to layout]
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.title,alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.image,alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.tutorial,alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.play,alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch()

        # [Adding ID]
        self.title.setObjectName("titleLabel")

        # [Connect buttons]
        self.play.clicked.connect(self.game_screen_func)
        self.tutorial.clicked.connect(self.tutorial_screen_func)

        # [Adding QSS]
        self.setStyleSheet("""
                QWidget {
                    background-color: #dddddd;
                    color: #0f172a;
                    font-family: "Segoe UI", system-ui, sans-serif;
                }

                QLabel#titleLabel {
                    color: #0f172a;
                    font-size: 20px;
                    font-weight: 500;
                    background: transparent;
                }

                QPushButton {
                    background-color: #11a4ff;
                    color: #ffffff;
                    border: 1px solid #dbe2ea;
                    border-radius: 8px;
                    font-size: 15px;
                    font-weight: 600;
                }

                QPushButton:hover {
                    background-color: #0e8bd9;
                    border-color: #cbd5e1;
                }

                QPushButton:pressed {
                    background-color: #0c74b4;
                }""")

    def tutorial_screen_func(self):
        from tutorial.united import UnitedTutorialScreen
        self.tutorial_screen = UnitedTutorialScreen()
        self.close()
        self.tutorial_screen.show()

    def game_screen_func(self):
        self.game_screen = TheHangmanScreen()
        self.close()
        self.game_screen.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IntroScreen()
    window.show()
    sys.exit(app.exec_())
