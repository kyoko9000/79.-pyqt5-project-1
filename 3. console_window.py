# ************************** man hinh loai 2 *************************
import os
import sys

from PyQt5 import QtGui, QtCore
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from gui2 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.textEdit.setText("hello")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.uic.textEdit.setFont(font)

        self.lineedit = QLineEdit(self.uic.centralwidget)
        self.lineedit.setGeometry(QtCore.QRect(10, 480, 200, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineedit.setFont(font)

        self.uic.pushButton.clicked.connect(self.runcommand)

    def runcommand(self):
        command = self.lineedit.text()
        text = os.popen(command)
        self.uic.textEdit.setText(text.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())