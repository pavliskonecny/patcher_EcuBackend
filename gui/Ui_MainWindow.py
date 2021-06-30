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
        MainWindow.setMaximumSize(QSize(570, 300))
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.btnInstall = QPushButton(self.centralwidget)
        self.btnInstall.setObjectName(u"btnInstall")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnInstall.setFont(font)
        self.btnInstall.setStyleSheet(u":enabled {\n"
" color:  rgb(0, 73, 122);\n"
"background-color: rgb(226, 182, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.btnInstall)

        self.btnUninstall = QPushButton(self.centralwidget)
        self.btnUninstall.setObjectName(u"btnUninstall")
        self.btnUninstall.setFont(font)
        self.btnUninstall.setStyleSheet(u":enabled {\n"
" color:  rgb(0, 73, 122);\n"
"background-color: rgb(226, 182, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.btnUninstall)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.lbl_patch_number = QLabel(self.centralwidget)
        self.lbl_patch_number.setObjectName(u"lbl_patch_number")

        self.gridLayout_2.addWidget(self.lbl_patch_number, 1, 0, 1, 1)

        self.lbl_patch_decription = QLabel(self.centralwidget)
        self.lbl_patch_decription.setObjectName(u"lbl_patch_decription")

        self.gridLayout_2.addWidget(self.lbl_patch_decription, 2, 0, 1, 1)

        self.lbl_patch_project = QLabel(self.centralwidget)
        self.lbl_patch_project.setObjectName(u"lbl_patch_project")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.lbl_patch_project.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_patch_project, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.lblLogo = QLabel(self.centralwidget)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setEnabled(True)
        self.lblLogo.setMaximumSize(QSize(80, 58))
        self.lblLogo.setCursor(QCursor(Qt.ArrowCursor))
        self.lblLogo.setFrameShape(QFrame.NoFrame)
        self.lblLogo.setPixmap(QPixmap(u":/icons/images/logo-hella.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setWordWrap(True)

        self.horizontalLayout.addWidget(self.lblLogo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.txeOutput = QPlainTextEdit(self.centralwidget)
        self.txeOutput.setObjectName(u"txeOutput")
        self.txeOutput.setEnabled(True)
        self.txeOutput.setReadOnly(True)

        self.verticalLayout.addWidget(self.txeOutput)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Patcher for EcuBackend 1.0", None))
        self.btnInstall.setText(QCoreApplication.translate("MainWindow", u"INSTALL\n"
"patch", None))
        self.btnUninstall.setText(QCoreApplication.translate("MainWindow", u"UNINSTALL\n"
"patch", None))
        self.lbl_patch_number.setText(QCoreApplication.translate("MainWindow", u"Patch_number", None))
        self.lbl_patch_decription.setText(QCoreApplication.translate("MainWindow", u"Patch_description", None))
        self.lbl_patch_project.setText(QCoreApplication.translate("MainWindow", u"Patch_project", None))
        self.lblLogo.setText("")
        self.txeOutput.setPlainText(QCoreApplication.translate("MainWindow", u"Output text...", None))
    # retranslateUi

