import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication
from pathlib import Path
from qdarkstyle import LightPalette
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]
sys.path.append(str(ROOT))
print(ROOT)
from windows.loginWindow import LoginMw

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
    loginMw = LoginMw()
    app.exec()
