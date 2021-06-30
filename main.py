from PySide2.QtWidgets import QApplication
from gui.MainWindow import MainWindow

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
