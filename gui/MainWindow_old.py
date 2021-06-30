"""
to convert from qt designer *.ui file to python *.py file use command:
pyuic5 --from-imports -o gui/Ui_MainWindow.py gui/Ui_MainWindow.ui

to convert resources file *.qrc to python *.py file use command:
pyrcc5 gui/resources.qrc -o gui/resources_rc.py
"""

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from gui.Ui_MainWindow import Ui_MainWindow
import files


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.btnInstall.clicked.connect(self.btnInstall_clicked)
        self.ui.btnUninstall.clicked.connect(self.btnUninstall_clicked)

        # init window
        self.ui.lbl_patch_project.setText(files.get_patch_project())
        self.ui.lbl_patch_number.setText(files.get_patch_number())
        self.ui.lbl_patch_decription.setText(files.get_patch_description())
        self.ui.txeOutput.setPlainText("")

    def btnInstall_clicked(self):
        try:
            self.ui.txeOutput.setPlainText("*** START INSTALLING PATCH ***")

            msg = files.check_destination_files()
            self.ui.txeOutput.appendPlainText(msg)

            msg = files.backup_files()
            self.ui.txeOutput.appendPlainText(msg)

            msg = files.replace_files()
            self.ui.txeOutput.appendPlainText(msg)

            self.ui.txeOutput.appendPlainText("*** INSTALLING PATCH WAS SUCCESSFUL ***")
            QMessageBox.information(self, "Done", f"Install patch complete!")
        except Exception as e:
            self.ui.txeOutput.appendPlainText("*** ERROR - INSTALLING PATCH WAS NOT SUCCESSFUL ***")
            QMessageBox.critical(self, "Error", f"INSTALLING PATCH WAS NOT SUCCESSFUL:\n{e}")

    def btnUninstall_clicked(self):
        try:
            self.ui.txeOutput.setPlainText("*** START UNINSTALLING PATCH ***")

            msg = files.restore_backup_files()
            self.ui.txeOutput.appendPlainText(msg)

            self.ui.txeOutput.appendPlainText("*** UNINSTALLING PATCH WAS SUCCESSFUL ***")
            QMessageBox.information(self, "Done", f"Uninstall patch complete!")
        except Exception as e:
            self.ui.txeOutput.appendPlainText("*** ERROR - UNINSTALLING PATCH WAS NOT SUCCESSFUL ***")
            QMessageBox.critical(self, "Error", f"UNINSTALLING PATCH WAS NOT SUCCESSFUL:\n{e}")
