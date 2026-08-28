"""XXX screen module"""

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

class RuleTwoScreen(QWidget):
    go_next_screen = pyqtSignal()
    go_previous_screen = pyqtSignal()
    def __init__(self):
        super().__init__()
        # [Loading language dict]
        self.language = load_language(LANGUAGE_CODE)

        # [Basic game boilerplate]
        self.setWindowTitle(self.language["title"])
        self.setGeometry(700, 300, 600, 600)

        # [Title]
        self.title = QLabel(self.language["rule2"])
        self.title.setObjectName("defeatTitle")
        self.title.setWordWrap(False)

        # [Images]
        self.image = QLabel()
        self.pixmap = QPixmap(str(get_assets_route("assets/images_tutorial/rule_2.png"))).scaled(450, 450, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image.setPixmap(self.pixmap)

        # [Buttons]
        self.next_arrow = QPushButton(">")
        self.next_arrow.setObjectName("primaryButton")

        self.previous_arrow = QPushButton("<")
        self.previous_arrow.setObjectName("secondaryButton")

        for btn in (self.next_arrow,self.previous_arrow):
            btn.setFixedHeight(40)
            btn.setFixedWidth(40)
            btn.setCursor(Qt.PointingHandCursor)

        self.next_arrow.clicked.connect(lambda: self.go_next_screen.emit())
        self.previous_arrow.clicked.connect(lambda: self.go_previous_screen.emit())

        # [Layout structure]
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(20)
        self.setLayout(self.main_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.previous_arrow)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.next_arrow)
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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RuleTwoScreen()
    window.show()
    sys.exit(app.exec_())