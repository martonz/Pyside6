from PySide6.QtWidgets import QApplication, QWidget
# Open an Empty Window
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()