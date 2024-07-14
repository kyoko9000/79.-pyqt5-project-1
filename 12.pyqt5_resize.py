# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui5 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ratio_h = 1
        self.ratio_w = 1
        self.new_x_button_1 = None
        self.new_x_button = None

        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.load_image)

        self.old_screen_w = self.geometry().width()
        self.old_screen_h = self.geometry().height()

    def load_image(self):
        # Tải ảnh và đặt vào QLabel
        pixmap = QPixmap("1.jpg")
        self.uic.label.setPixmap(pixmap)

    def changeEvent(self, a0):
        self.button_calculate()

    def resizeEvent(self, event):
        self.new_button_ratio()
        self.button_calculate()
        self.font_button()

    def new_button_ratio(self):
        # frame width
        new_screen_w = self.geometry().width()
        new_screen_h = self.geometry().height()
        self.ratio_w = round((new_screen_w / self.old_screen_w), 2)
        self.ratio_h = round((new_screen_h / self.old_screen_h), 2)

    def button_calculate(self):
        # frame width
        new_screen_w = self.geometry().width()

        # calculate x coordinates of center button
        center_x_button = int(new_screen_w / 3)
        center_x_button_1 = int(new_screen_w * 2 / 3)

        # calculate new x,y button base on center button
        self.new_button_pos(center_x_button, center_x_button_1)

    def new_button_pos(self, center_x_button, center_x_button_1):
        rect = self.uic.pushButton.geometry()
        self.new_x_button = center_x_button - rect.width() // 2
        self.new_x_button_1 = center_x_button_1 - rect.width() // 2
        self.new_button()

    def new_button(self):
        self.uic.pushButton.setGeometry(self.new_x_button, 40, int(121*self.ratio_w), int(61*self.ratio_h))
        self.uic.pushButton_2.setGeometry(self.new_x_button_1, 40, int(111*self.ratio_w), int(61*self.ratio_h))

    def font_button(self):
        # Tạo font và áp dụng cho QPushButton
        font = QFont("Arial", int(20*self.ratio_w), QFont.Bold)
        self.uic.pushButton.setFont(font)
        self.uic.pushButton_2.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
