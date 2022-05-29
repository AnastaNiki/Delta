# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(289, 331)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        Info.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Info)
        self.gridLayout.setObjectName("gridLayout")
        self.text = QtWidgets.QTextBrowser(Info)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 0, 0, 1, 1)

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Свойства"))
