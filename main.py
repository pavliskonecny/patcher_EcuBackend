"""***********************************************************************"""
"""*** The app for replacing EcuBackend source files ***"""
"""***********************************************************************"""
"""
from PyQt5 import QtWidgets
from gui.MainWindow import MainWindow
import sys


app = QtWidgets.QApplication([])
window = MainWindow()
sys.exit(app.exec())
"""

from PySide2.QtWidgets import*
#from PySide2.QtWidgets import QApplication
from gui.MainWidget import MainWidget

app = QApplication([])
window = MainWidget()
window.show()
app.exec_()
