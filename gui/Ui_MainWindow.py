# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(570, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(570, 300))
        MainWindow.setMaximumSize(QSize(1000, 900))
        icon = QIcon()
        icon.addFile(u":/main ico/images/MateoEcuServer.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lay_header = QHBoxLayout()
        self.lay_header.setObjectName(u"lay_header")
        self.lay_header.setContentsMargins(0, -1, 0, -1)
        self.lay_buttons = QVBoxLayout()
        self.lay_buttons.setSpacing(10)
        self.lay_buttons.setObjectName(u"lay_buttons")
        self.lay_buttons.setSizeConstraint(QLayout.SetFixedSize)
        self.lay_buttons.setContentsMargins(-1, -1, 0, -1)
        self.btn_install = QPushButton(self.centralwidget)
        self.btn_install.setObjectName(u"btn_install")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_install.setFont(font)
        self.btn_install.setStyleSheet(u":enabled {\n"
" color:  rgb(0, 73, 122);\n"
"background-color: rgb(226, 182, 0);\n"
"}")

        self.lay_buttons.addWidget(self.btn_install)

        self.btn_uninstall = QPushButton(self.centralwidget)
        self.btn_uninstall.setObjectName(u"btn_uninstall")
        self.btn_uninstall.setFont(font)
        self.btn_uninstall.setStyleSheet(u":enabled {\n"
" color:  rgb(0, 73, 122);\n"
"background-color: rgb(226, 182, 0);\n"
"}")

        self.lay_buttons.addWidget(self.btn_uninstall)


        self.lay_header.addLayout(self.lay_buttons)

        self.lay_info = QGridLayout()
        self.lay_info.setObjectName(u"lay_info")
        self.lay_info.setContentsMargins(0, -1, 0, -1)
        self.lbl_patch_number = QLabel(self.centralwidget)
        self.lbl_patch_number.setObjectName(u"lbl_patch_number")

        self.lay_info.addWidget(self.lbl_patch_number, 1, 0, 1, 1)

        self.lbl_patch_decription = QLabel(self.centralwidget)
        self.lbl_patch_decription.setObjectName(u"lbl_patch_decription")

        self.lay_info.addWidget(self.lbl_patch_decription, 2, 0, 1, 1)

        self.lbl_patch_project = QLabel(self.centralwidget)
        self.lbl_patch_project.setObjectName(u"lbl_patch_project")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.lbl_patch_project.setFont(font1)

        self.lay_info.addWidget(self.lbl_patch_project, 0, 0, 1, 1)


        self.lay_header.addLayout(self.lay_info)

        self.lbl_logo = QLabel(self.centralwidget)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setEnabled(True)
        self.lbl_logo.setMaximumSize(QSize(80, 58))
        self.lbl_logo.setCursor(QCursor(Qt.ArrowCursor))
        self.lbl_logo.setFrameShape(QFrame.NoFrame)
        self.lbl_logo.setPixmap(QPixmap(u":/icons/images/logo-hella.png"))
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setWordWrap(True)

        self.lay_header.addWidget(self.lbl_logo)


        self.verticalLayout.addLayout(self.lay_header)

        self.txe_output = QPlainTextEdit(self.centralwidget)
        self.txe_output.setObjectName(u"txe_output")
        self.txe_output.setEnabled(True)
        self.txe_output.setReadOnly(True)

        self.verticalLayout.addWidget(self.txe_output)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Patcher for EcuBackend 1.0", None))
        self.btn_install.setText(QCoreApplication.translate("MainWindow", u"INSTALL\n"
"patch", None))
        self.btn_uninstall.setText(QCoreApplication.translate("MainWindow", u"UNINSTALL\n"
"patch", None))
        self.lbl_patch_number.setText(QCoreApplication.translate("MainWindow", u"Patch_number", None))
        self.lbl_patch_decription.setText(QCoreApplication.translate("MainWindow", u"Patch_description", None))
        self.lbl_patch_project.setText(QCoreApplication.translate("MainWindow", u"Patch_project", None))
        self.lbl_logo.setText("")
        self.txe_output.setPlainText(QCoreApplication.translate("MainWindow", u"Output text...", None))
    # retranslateUi

