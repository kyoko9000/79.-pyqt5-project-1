# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.radioButton.clicked.connect(self.show_funtion)
        self.uic.spinBox.textChanged.connect(self.show_num)

    def show_num(self):
        num = self.uic.spinBox.text()
        self.uic.lineEdit.setText(num)

    def show_funtion(self, click):
        if click:
            print("on")
            # read text
            # text = self.uic.spinBox.text()
            # print(text)

            # set value
            self.uic.spinBox.setValue(50)
        else:
            print("off")
            # clear spinbox
            self.uic.spinBox.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
