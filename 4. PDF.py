# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtPrintSupport import QPrinter
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from gui2 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.printPDF)
        a = 28
        image = '1.jpg'
        self.uic.textEdit.setHtml(
            f"<p>{a}</p>\n"
            f"<p style='margin-left:200px;'><img src={image} width='300' height='300'></p>\n"
            "<p>this is test app</p>"
        )

    def printPDF(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', "file1.pdf", '*.pdf')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(fn)
        self.uic.textEdit.document().print_(printer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())