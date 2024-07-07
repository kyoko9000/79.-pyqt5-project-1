# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtCore import QDate
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget
from gui3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.choose_date)

        # creating a QCalendarWidget object
        self.calendar = QCalendarWidget(self.uic.centralwidget)
        self.uic.verticalLayout.addWidget(self.calendar)

        self.calendar.clicked.connect(self.show_date)

    def show_date(self):
        # show day, mouth, year
        # print(self.calendar.selectedDate().getDate())
        # show day
        # print(self.calendar.selectedDate().day())
        # show mouth
        # print(self.calendar.selectedDate().month())
        # show year
        print(self.calendar.selectedDate().year())

    def choose_date(self):
        # show month of calendar now
        # self.calendar.showToday()

        # show any day we choose
        # date = QDate(2021, 8, 10)  # Thay đổi ngày và tháng tùy ý
        # self.calendar.setSelectedDate(date)

        # show today
        self.calendar.setSelectedDate(QDate.currentDate())

        # print today
        # print(QDate.currentDate().getDate())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())