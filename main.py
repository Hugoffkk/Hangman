import sys
from introduction.intro_screen import IntroScreen
from PyQt5.QtWidgets import (QApplication)

app = QApplication(sys.argv)
window = IntroScreen()
window.show()
sys.exit(app.exec_())