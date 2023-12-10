# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from gui2 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.printpreviewDialog)
        a = 28
        image = '1.jpg'
        self.uic.textEdit.setHtml(
            f"<p>{a}</p>\n"
            "<p style=' margin-top:0px; margin-bottom:0px; margin-left:100px; margin-right:0px;'>111111</p>\n"
            f"<p align='center'>22222</p>\n"
            f"<p align='right'>33333</p>"
            f"<p style='margin-left:200px;'><img src={image} width='300' height='300'></p>\n"
            "<p>this is test app</p>"
        )

    def printPDF(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', "file1.pdf", '*.pdf')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(fn)
        self.uic.textEdit.document().print_(printer)

    def printpreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self, printer):
        self.uic.textEdit.print_(printer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())