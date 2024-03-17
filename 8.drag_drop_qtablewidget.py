# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtCore import Qt
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView

from gui4 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.pushButton.clicked.connect(self.set_drag_drop)
        # self.uic.tableWidget.setSortingEnabled(True)

        self.uic.pushButton.setText("drag drop")

        # add data to QtableWidget
        list1 = [20, 35, 1, 4]
        list2 = [50, 6, 71, 8]
        for i in range(4):
            # set data at int
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, int(list1[i]))
            self.uic.tableWidget.setItem(i, 0, item)
            # set data at str
            self.uic.tableWidget.setItem(i, 1, QTableWidgetItem(str(list2[i])))

    def set_drag_drop(self):
        #Kích hoạt chức năng kéo thả column
        self.uic.tableWidget.horizontalHeader().setSectionsMovable(True)
        self.uic.tableWidget.horizontalHeader().setDragDropMode(QAbstractItemView.InternalMove)
        self.uic.tableWidget.horizontalHeader().setAcceptDrops(True)

        # Kích hoạt chức năng kéo thả row
        self.uic.tableWidget.verticalHeader().setSectionsMovable(True)
        self.uic.tableWidget.verticalHeader().setDragDropMode(QAbstractItemView.InternalMove)
        self.uic.tableWidget.verticalHeader().setAcceptDrops(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

