"""
to convert from qt designer *.ui file to python *.py file use command:
pyside2-uic --from-imports gui/Ui_MainWindow.ui -o gui/Ui_MainWindow.py

to convert resources file *.qrc to python *.py file use command:
pyside2-rcc -g python gui/resources.qrc > gui/resources_rc.py
"""

from PySide2.QtWidgets import*
from gui.Ui_MainWindow import Ui_MainWindow
from PatchFiles import PatchFiles


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_install.clicked.connect(self.btn_install_clicked)
        self.ui.btn_uninstall.clicked.connect(self.btn_uninstall_clicked)

        # init window
        self.ui.lbl_patch_project.setText(PatchFiles.PATCH_PROJECT)
        self.ui.lbl_patch_number.setText(PatchFiles.PATCH_NUMBER)
        self.ui.lbl_patch_decription.setText(PatchFiles.PATCH_DESCRIPTION)
        self.ui.txe_output.setPlainText("")

    def btn_install_clicked(self):
        try:
            self.ui.txe_output.setPlainText("*** START INSTALLING PATCH ***")
            pf = PatchFiles()

            msg = pf.check_destination_files()
            self.ui.txe_output.appendPlainText(msg)

            msg = pf.backup_files()
            self.ui.txe_output.appendPlainText(msg)

            msg = pf.replace_files()
            self.ui.txe_output.appendPlainText(msg)

            self.ui.txe_output.appendPlainText("*** INSTALLING PATCH WAS SUCCESSFUL ***")
            QMessageBox.information(self, "Done", f"Install patch complete!")
        except Exception as e:
            self.ui.txe_output.appendPlainText("*** ERROR - INSTALLING PATCH WAS NOT SUCCESSFUL ***")
            QMessageBox.critical(self, "Error", f"INSTALLING PATCH WAS NOT SUCCESSFUL:\n{e}")

    def btn_uninstall_clicked(self):
        try:
            self.ui.txe_output.setPlainText("*** START UNINSTALLING PATCH ***")
            pf = PatchFiles()

            msg = pf.restore_backup_files()
            self.ui.txe_output.appendPlainText(msg)

            self.ui.txe_output.appendPlainText("*** UNINSTALLING PATCH WAS SUCCESSFUL ***")
            QMessageBox.information(self, "Done", f"Uninstall patch complete!")
        except Exception as e:
            self.ui.txe_output.appendPlainText("*** ERROR - UNINSTALLING PATCH WAS NOT SUCCESSFUL ***")
            QMessageBox.critical(self, "Error", f"UNINSTALLING PATCH WAS NOT SUCCESSFUL:\n{e}")
