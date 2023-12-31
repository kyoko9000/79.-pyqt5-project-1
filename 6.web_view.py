# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from gui3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.web = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.loadweb)

    def loadweb(self):
        self.web = QWebEngineView()
        self.web.load(QUrl('https://www.google.com/'))
        lay = QVBoxLayout(self.uic.frame)
        lay.addWidget(self.web)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())