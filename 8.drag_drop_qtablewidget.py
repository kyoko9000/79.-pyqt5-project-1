from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView


class MyTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.new_column = None
        self.setColumnCount(3)
        self.setRowCount(5)
        self.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])

        # Đặt dữ liệu vào cột 0 (vị trí hiện tại)
        for row in range(5):
            item = QTableWidgetItem(f"Data {row}")
            self.setItem(row, 0, item)

        # Kích hoạt chức năng kéo thả column
        self.horizontalHeader().setSectionsMovable(True)
        self.horizontalHeader().setDragDropMode(QAbstractItemView.InternalMove)
        self.horizontalHeader().setAcceptDrops(True)

        # Kích hoạt chức năng kéo thả row
        self.verticalHeader().setSectionsMovable(True)
        self.verticalHeader().setDragDropMode(QAbstractItemView.InternalMove)
        self.verticalHeader().setAcceptDrops(True)  # hi


if __name__ == '__main__':
    app = QApplication([])
    table = MyTableWidget()
    table.show()
    app.exec_()
