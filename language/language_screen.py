"""Language Screen"""

import sys,qdarktheme
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QVBoxLayout)
from helpers.lang_config import LANGUAGE_CODE
from helpers.load_lang import load_language

class LanguageScreen(QWidget):
    def __init__(self):
        super().__init__()
        # [Loading language dict]
        self.language = load_language(LANGUAGE_CODE)

        # [Basic game boilerplate]
        self.setWindowTitle(self.language["title"])
        self.setGeometry(700,300,400,400)

        # [Layout]

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)

        # [Title]
        self.title = QLabel("Select a language")

        self.btn_english = QPushButton("English 🇬🇧")
        self.btn_spanish = QPushButton("Spanish 🇪🇸")
        self.btn_french = QPushButton("French 🇫🇷")

        for btn in (self.btn_english, self.btn_spanish, self.btn_french):
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedHeight(40)
            btn.setFixedWidth(120)

        # [Adding to layout]
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.btn_english, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.btn_spanish, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.btn_french, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch()

        # [Adding ID]
        self.title.setObjectName("titleLabel")

        # [Connect buttons]
        self.btn_english.clicked.connect(lambda: self.set_code("en"))
        self.btn_spanish.clicked.connect(lambda: self.set_code("es"))
        self.btn_french.clicked.connect(lambda: self.set_code("fr"))

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
    def set_code(self,code: str) -> None:
        with open("helpers/lang_config.py","w") as f:
            f.write(f'LANGUAGE_CODE = "{code}"')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LanguageScreen()
    window.show()
    sys.exit(app.exec_())