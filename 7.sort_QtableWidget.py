# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtCore import Qt
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from gui4 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton_2.clicked.connect(self.decrease)
        self.uic.pushButton.clicked.connect(self.increase)
        self.uic.tableWidget.setSortingEnabled(True)

        list1 = [20, 35, 1, 4]
        list2 = [50, 6, 71, 8]
        for i in range(4):
            # set data at int
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, int(list1[i]))
            self.uic.tableWidget.setItem(i, 0, item)
            # set data at str
            self.uic.tableWidget.setItem(i, 1, QTableWidgetItem(str(list2[i])))

    def decrease(self):
        self.uic.tableWidget.sortItems(0, Qt.DescendingOrder)

    def increase(self):
        self.uic.tableWidget.sortItems(0, Qt.AscendingOrder)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())