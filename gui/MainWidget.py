"""
to convert from qt designer *.ui file to python *.py file use command:
pyside2-uic gui/Ui_MainWindow.ui -o gui/Ui_MainWindow.py

to convert resources file *.qrc to python *.py file use command:
pyrcc5 gui/resources.qrc -o gui/resources_rc.py
"""

from PySide2.QtWidgets import*
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import files
from gui.Ui_MainWindow import Ui_MainWindow


class MainWidget(QWidget):
    def __init__(self):
        """
        super(MainWidget, self).__init__()
        designer_file = QFile("gui\\Ui_MainWindow2.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(designer_file, self)
        designer_file.close()
        """

        super(MainWidget, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        #self.ui.setupUi(self)
        #self.show()

        self.ui.btnInstall.clicked.connect(self.btnInstall_clicked)
        self.ui.btnUninstall.clicked.connect(self.btnUninstall_clicked)
        """
        # init window
        self.ui.lbl_patch_project.setText(files.get_patch_project())
        self.ui.lbl_patch_number.setText(files.get_patch_number())
        self.ui.lbl_patch_decription.setText(files.get_patch_description())
        self.ui.txeOutput.setPlainText("")"""

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
