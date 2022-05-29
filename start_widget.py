# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_start_window(object):
    def setupUi(self, start_window):
        start_window.setObjectName("start_window")
        start_window.setWindowModality(QtCore.Qt.NonModal)
        start_window.setEnabled(True)
        start_window.resize(550, 157)
        start_window.setMinimumSize(QtCore.QSize(275, 157))
        start_window.setMaximumSize(QtCore.QSize(550, 157))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        start_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        start_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(start_window)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(40, 45, 200, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.start_button.setFont(font)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setObjectName("start_button")
        self.result_button = QtWidgets.QPushButton(self.centralwidget)
        self.result_button.setGeometry(QtCore.QRect(310, 45, 200, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.result_button.setFont(font)
        self.result_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.result_button.setObjectName("result_button")
        start_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(start_window)
        QtCore.QMetaObject.connectSlotsByName(start_window)

    def retranslateUi(self, start_window):
        _translate = QtCore.QCoreApplication.translate
        start_window.setWindowTitle(_translate("start_window", "Количество моржей"))
        self.start_button.setText(_translate("start_window", "Выбрать новые фото"))
        self.result_button.setText(_translate("start_window", "Посмотреть результаты"))
