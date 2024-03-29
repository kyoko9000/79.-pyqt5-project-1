# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.add_items)
        self.uic.pushButton_2.clicked.connect(self.edit_items)
        self.uic.pushButton_3.clicked.connect(self.delete_items)
        self.uic.pushButton_4.clicked.connect(self.clear_all)
        self.list = []

        f = open("1_home_number.txt", "r")
        self.home_number_list = f.read()
        # print("hhhh", self.home_number_list)
        for item in self.home_number_list:
            if item != "\n":
                self.uic.listWidget.addItem(f"home: {item}")
                self.list.append(item)
        print(self.list)

    def add_items(self):
        home_number = self.uic.lineEdit.text()
        self.uic.listWidget.addItem(f"home: {home_number}")
        self.list.append(home_number)
        print(self.list)
        self.write_list()

    def edit_items(self):
        home_number = self.uic.lineEdit.text()
        item = self.uic.listWidget.currentItem()
        item.setText(f"home: {home_number}")

        row = self.uic.listWidget.currentRow()
        self.list[row] = home_number
        print(self.list)
        self.write_list()

    def delete_items(self):
        row = self.uic.listWidget.currentRow()
        self.uic.listWidget.takeItem(row)
        self.list.pop(row)
        self.write_list()
        print(self.list)

    def clear_all(self):
        self.uic.listWidget.clear()
        a_file = open("1_home_number.txt", "w")
        a_file.write("")
        self.list = []
        print(self.list)

    def write_list(self):
        a_file = open("1_home_number.txt", "w")
        a_file.write("")
        for i in self.list:
            a_file = open("1_home_number.txt", "a")
            a_file.write(f"{i}\n")
            a_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())