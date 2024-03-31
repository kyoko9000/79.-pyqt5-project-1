import sys
import time

import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from gui3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):  # Show GUI
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.label = QtWidgets.QLabel(self.uic.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.label.setFont(font)
        self.label.setText("this is a label")
        self.uic.verticalLayout.addWidget(self.label)

        self.Button = QtWidgets.QPushButton(self.uic.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Button.setFont(font)
        self.Button.setText("update")
        self.uic.verticalLayout.addWidget(self.Button)

        self.Button1 = QtWidgets.QPushButton(self.uic.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Button1.setFont(font)
        self.Button1.setText("stop")
        self.uic.verticalLayout.addWidget(self.Button1)

        self.uic.pushButton.setText("start")

        self.uic.pushButton.clicked.connect(self.start_thread)
        self.Button1.clicked.connect(self.stop_thread)
        self.Button.clicked.connect(self.update_value)
        self.thread = {}

    def start_thread(self):
        self.thread[1] = thread_section(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.show_data)

    def stop_thread(self):
        self.thread[1].stop_app()

    def show_data(self, data):
        self.label.setText(str(data))

    def update_value(self):
        number = 2
        self.thread[1].update_data(number)

class thread_section(QThread):
    signal = pyqtSignal(object)

    def __init__(self, index):
        self.i = 0
        self.up = False
        self.data = None
        self.stop = False
        self.index = index
        print("Starting threading: ", self.index)
        super().__init__()

    def run(self):
        while True:
            self.i += 1
            time.sleep(1)
            print(self.i)
            self.signal.emit(self.i)

            # update data
            if self.up:
                self.i = self.data
                self.up = False
            # stop program
            if self.stop:
                break

    def stop_app(self):
        print("stop")
        self.stop = True

    def update_data(self, data):
        self.up = True
        self.data = data
        print("update", self.data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
