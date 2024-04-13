# ************************** man hinh loai 2 *************************
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QSlider
from gui3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pixmap = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.setsize)

        self.lineedit = QLineEdit(self.uic.frame)
        self.lineedit.setGeometry(QtCore.QRect(800, 10, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineedit.setFont(font)
        self.lineedit.setText("300")

        self.label = QLabel(self.uic.frame)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setGeometry(QtCore.QRect(10, 10, 600, 500))
        self.pixmap = QPixmap("2.jpg")
        self.opset = 120
        w = self.label.size().width() - self.opset
        h = self.label.size().height() - self.opset
        scaled = self.pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self.label.setPixmap(scaled)

        # Create a QSlider to control the rotation
        self.slider = QSlider(self.uic.frame)
        self.slider.setGeometry(QtCore.QRect(700, 80, 200, 25))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        # Set the minimum and maximum values of the slider to 0 and 360 degrees, respectively
        self.slider.setMinimum(0)
        self.slider.setMaximum(360)
        # Set the initial value of the slider to 0 degrees
        self.slider.setValue(0)

        # Connect the valueChanged signal of the slider to the rotate_image method
        self.slider.valueChanged.connect(self.rotate_image)

        # Create a QSlider to control the rotation
        self.slider1 = QSlider(self.uic.frame)
        self.slider1.setGeometry(QtCore.QRect(700, 150, 200, 25))
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        # Set the minimum and maximum values of the slider to 0 and 360 degrees, respectively
        self.slider1.setMinimum(300)
        self.slider1.setMaximum(800)
        # Set the initial value of the slider to 0 degrees
        self.slider1.setValue(300)

        # Connect the valueChanged signal of the slider to the rotate_image method
        self.slider1.valueChanged.connect(self.setsize1)

    def setsize(self):
        size = self.lineedit.text()
        self.label.setGeometry(QtCore.QRect(10, 10, 600, int(size)))
        self.pixmap = QPixmap("2.jpg")
        w = self.label.size().width() - self.opset
        h = self.label.size().height() - self.opset
        scaled = self.pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self.label.setPixmap(scaled)

    def setsize1(self, num):
        self.label.setGeometry(QtCore.QRect(10, 10, 600, num))
        self.pixmap = QPixmap("2.jpg")
        w = self.label.size().width() - self.opset
        h = self.label.size().height() - self.opset
        scaled = self.pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self.label.setPixmap(scaled)

    def rotate_image(self, angle):
        # Create a QTransform object that will rotate the image around its center point by the given angle
        transform = QTransform().rotate(angle)
        # Apply the transformation to the image and create a new QPixmap object
        w = self.label.size().width() - self.opset
        h = self.label.size().height() - self.opset
        scaled = self.pixmap.scaled(w, h, Qt.KeepAspectRatio)
        rotated_image = scaled.transformed(transform, Qt.SmoothTransformation)
        # Set the rotated image as the pixmap of the QLabel
        self.label.setPixmap(rotated_image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())