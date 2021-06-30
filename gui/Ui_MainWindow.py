# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(570, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(570, 300))
        MainWindow.setMaximumSize(QtCore.QSize(570, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main ico/images/MateoEcuServer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnInstall = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnInstall.setFont(font)
        self.btnInstall.setStyleSheet(":enabled {\n"
" color:  rgb(0, 73, 122);\n"
"background-color: rgb(226, 182, 0);\n"
"}")
        self.btnInstall.setObjectName("btnInstall")
        self.verticalLayout_2.addWidget(self.btnInstall)
        self.btnUninstall = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnUninstall.setFont(font)
        self.btnUninstall.setStyleSheet(":enabled {\n"
" color:  rgb(0, 73, 122);\n"
"background-color: rgb(226, 182, 0);\n"
"}")
        self.btnUninstall.setObjectName("btnUninstall")
        self.verticalLayout_2.addWidget(self.btnUninstall)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_patch_number = QtWidgets.QLabel(self.centralwidget)
        self.lbl_patch_number.setObjectName("lbl_patch_number")
        self.gridLayout_2.addWidget(self.lbl_patch_number, 1, 0, 1, 1)
        self.lbl_patch_decription = QtWidgets.QLabel(self.centralwidget)
        self.lbl_patch_decription.setObjectName("lbl_patch_decription")
        self.gridLayout_2.addWidget(self.lbl_patch_decription, 2, 0, 1, 1)
        self.lbl_patch_project = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_patch_project.setFont(font)
        self.lbl_patch_project.setObjectName("lbl_patch_project")
        self.gridLayout_2.addWidget(self.lbl_patch_project, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLogo.setEnabled(True)
        self.lblLogo.setMaximumSize(QtCore.QSize(80, 58))
        self.lblLogo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lblLogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/icons/images/logo-hella.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setWordWrap(True)
        self.lblLogo.setObjectName("lblLogo")
        self.horizontalLayout.addWidget(self.lblLogo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.txeOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txeOutput.setEnabled(True)
        self.txeOutput.setReadOnly(True)
        self.txeOutput.setObjectName("txeOutput")
        self.verticalLayout.addWidget(self.txeOutput)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patcher for EcuBackend 1.0"))
        self.btnInstall.setText(_translate("MainWindow", "INSTALL\n"
"patch"))
        self.btnUninstall.setText(_translate("MainWindow", "UNINSTALL\n"
"patch"))
        self.lbl_patch_number.setText(_translate("MainWindow", "Patch_number"))
        self.lbl_patch_decription.setText(_translate("MainWindow", "Patch_description"))
        self.lbl_patch_project.setText(_translate("MainWindow", "Patch_project"))
        self.txeOutput.setPlainText(_translate("MainWindow", "Output text..."))
from . import resources_rc