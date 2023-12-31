# ************************** man hinh loai 2 *************************
import sys

from PyQt5 import QtCore
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget
from gui4 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())