import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Icons with Click Event")
        icons = sorted([attr for attr in dir(QStyle) if attr.startswith("SP_")])
        layout = QGridLayout()
        for n, name in enumerate(icons):
            btn = QPushButton(name)
            pixmapi = getattr(QStyle, name)
            icon = self.style().standardIcon(pixmapi)
            btn.setIcon(icon)
            btn.clicked.connect(self.button_clicked)  # Kết nối sự kiện nhấn nút
            layout.addWidget(btn, n // 4, n % 4)
        self.setLayout(layout)

    def button_clicked(self):
        button = self.sender()  # Lấy nút đã được nhấn
        print(f"Button clicked: {button.text()}")  # In ra tên của nút

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

