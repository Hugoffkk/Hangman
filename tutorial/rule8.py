import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, 
    QPushButton, QVBoxLayout, QHBoxLayout
)
from helpers.lang_config import LANGUAGE_CODE
from helpers.load_lang import load_language
from helpers.get_assets import get_assets_route


class RuleEightScreen(QWidget):
    go_to_menu = pyqtSignal()
    go_to_game = pyqtSignal()

    def __init__(self):
        super().__init__()
        # [Loading language dict]
        self.language = load_language(LANGUAGE_CODE)

        # [Basic game boilerplate]
        self.setWindowTitle(self.language["title"])
        self.setGeometry(700, 300, 600, 600)

        # [Title]
        self.title = QLabel(self.language["rule8"])
        self.title.setObjectName("defeatTitle")
        self.title.setWordWrap(False)

        # [Images]
        self.image = QLabel()
        self.pixmap = QPixmap(str(get_assets_route("assets/images_tutorial/rule_8.png"))).scaled(450, 450, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image.setPixmap(self.pixmap)

        # [Buttons]
        self.menu = QPushButton("Main menu")
        self.menu.setObjectName("primaryButton")

        self.game = QPushButton("Play")
        self.game.setObjectName("secondaryButton")

        for btn in (self.menu, self.game):
            btn.setFixedHeight(40)
            btn.setFixedWidth(140)
            btn.setCursor(Qt.PointingHandCursor)

        self.menu.clicked.connect(lambda: self.go_to_menu.emit())
        self.game.clicked.connect(lambda: self.go_to_game.emit())

        # [Layout structure]
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(20)
        self.setLayout(self.main_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.menu)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.game)
        self.buttons_layout.addStretch()

        self.main_layout.addStretch()
        self.main_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.image, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addStretch()

        # [Apply custom QSS styling]
        self.apply_styles()

    def apply_styles(self):
        qss = """
            #defeatTitle {
                font-size: 26px;
                font-weight: bold;
                color: #000000;
                padding: 10px;
            }
            QPushButton {
                font-size: 14px;
                font-weight: 600;
                border-radius: 8px;
            }
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RuleEightScreen()
    window.show()
    sys.exit(app.exec_())