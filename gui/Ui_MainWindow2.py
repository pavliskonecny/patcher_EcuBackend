# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(411, 278)
        self.btnInstall = QPushButton(Form)
        self.btnInstall.setObjectName(u"btnInstall")
        self.btnInstall.setGeometry(QRect(70, 30, 75, 23))
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(160, 30, 70, 17))
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 70, 381, 191))
        self.btnUninstall = QPushButton(Form)
        self.btnUninstall.setObjectName(u"btnUninstall")
        self.btnUninstall.setGeometry(QRect(260, 30, 75, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnInstall.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.btnUninstall.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

