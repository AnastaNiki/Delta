# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gallery_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(935, 920)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.main_right_arrow = QtWidgets.QPushButton(Form)
        self.main_right_arrow.setMinimumSize(QtCore.QSize(30, 100))
        self.main_right_arrow.setMaximumSize(QtCore.QSize(40, 40))
        self.main_right_arrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_right_arrow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/icon_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_right_arrow.setIcon(icon1)
        self.main_right_arrow.setIconSize(QtCore.QSize(40, 40))
        self.main_right_arrow.setFlat(True)
        self.main_right_arrow.setObjectName("main_right_arrow")
        self.gridLayout.addWidget(self.main_right_arrow, 5, 15, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 12, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 10, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 17, 0, 1, 1)
        self.main_left_arrow = QtWidgets.QPushButton(Form)
        self.main_left_arrow.setMinimumSize(QtCore.QSize(30, 100))
        self.main_left_arrow.setMaximumSize(QtCore.QSize(40, 40))
        self.main_left_arrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_left_arrow.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/icon_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_left_arrow.setIcon(icon2)
        self.main_left_arrow.setIconSize(QtCore.QSize(40, 40))
        self.main_left_arrow.setFlat(True)
        self.main_left_arrow.setObjectName("main_left_arrow")
        self.gridLayout.addWidget(self.main_left_arrow, 5, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout.addWidget(self.frame_3, 14, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout.addWidget(self.frame_4, 12, 15, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 14, 15, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 15, 8, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(0, 48))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.reset_button = QtWidgets.QPushButton(self.widget)
        self.reset_button.setMinimumSize(QtCore.QSize(30, 30))
        self.reset_button.setMaximumSize(QtCore.QSize(30, 30))
        self.reset_button.setSizeIncrement(QtCore.QSize(0, 0))
        self.reset_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/start_size.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon3)
        self.reset_button.setIconSize(QtCore.QSize(30, 30))
        self.reset_button.setFlat(True)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout.addWidget(self.reset_button)
        spacerItem4 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.plus_zoom = QtWidgets.QPushButton(self.widget)
        self.plus_zoom.setMinimumSize(QtCore.QSize(30, 30))
        self.plus_zoom.setMaximumSize(QtCore.QSize(30, 30))
        self.plus_zoom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plus_zoom.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus_zoom.setIcon(icon4)
        self.plus_zoom.setIconSize(QtCore.QSize(30, 30))
        self.plus_zoom.setFlat(True)
        self.plus_zoom.setObjectName("plus_zoom")
        self.horizontalLayout.addWidget(self.plus_zoom)
        spacerItem5 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.min_zoom = QtWidgets.QPushButton(self.widget)
        self.min_zoom.setMinimumSize(QtCore.QSize(30, 30))
        self.min_zoom.setMaximumSize(QtCore.QSize(30, 30))
        self.min_zoom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min_zoom.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.min_zoom.setIcon(icon5)
        self.min_zoom.setIconSize(QtCore.QSize(30, 30))
        self.min_zoom.setFlat(True)
        self.min_zoom.setObjectName("min_zoom")
        self.horizontalLayout.addWidget(self.min_zoom)
        spacerItem6 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.info_button = QtWidgets.QPushButton(self.widget)
        self.info_button.setMinimumSize(QtCore.QSize(30, 30))
        self.info_button.setMaximumSize(QtCore.QSize(30, 30))
        self.info_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.info_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/icon_i.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_button.setIcon(icon6)
        self.info_button.setIconSize(QtCore.QSize(30, 30))
        self.info_button.setFlat(True)
        self.info_button.setObjectName("info_button")
        self.horizontalLayout.addWidget(self.info_button)
        spacerItem7 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.gridLayout.addWidget(self.widget, 9, 0, 1, 16)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 3, 13, 1, 1)
        self.map_button = QtWidgets.QPushButton(self.widget_3)
        self.map_button.setMinimumSize(QtCore.QSize(120, 40))
        self.map_button.setMaximumSize(QtCore.QSize(120, 40))
        self.map_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.map_button.setObjectName("map_button")
        self.gridLayout_2.addWidget(self.map_button, 3, 4, 1, 1)
        self.result_button = QtWidgets.QPushButton(self.widget_3)
        self.result_button.setMinimumSize(QtCore.QSize(120, 40))
        self.result_button.setMaximumSize(QtCore.QSize(120, 40))
        self.result_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_button.setObjectName("result_button")
        self.gridLayout_2.addWidget(self.result_button, 3, 8, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 3, 2, 1, 1)
        self.count_button = QtWidgets.QPushButton(self.widget_3)
        self.count_button.setMinimumSize(QtCore.QSize(120, 40))
        self.count_button.setMaximumSize(QtCore.QSize(120, 40))
        self.count_button.setObjectName("count_button")
        self.gridLayout_2.addWidget(self.count_button, 3, 6, 1, 1)
        self.all_button = QtWidgets.QPushButton(self.widget_3)
        self.all_button.setMinimumSize(QtCore.QSize(120, 40))
        self.all_button.setMaximumSize(QtCore.QSize(120, 40))
        self.all_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.all_button.setObjectName("all_button")
        self.gridLayout_2.addWidget(self.all_button, 3, 5, 1, 1)
        self.allcount_button = QtWidgets.QPushButton(self.widget_3)
        self.allcount_button.setMinimumSize(QtCore.QSize(120, 40))
        self.allcount_button.setMaximumSize(QtCore.QSize(120, 40))
        self.allcount_button.setObjectName("allcount_button")
        self.gridLayout_2.addWidget(self.allcount_button, 3, 7, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 3, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.widget_3)
        self.frame_5.setMinimumSize(QtCore.QSize(160, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(0, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.frame_5, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 16, 0, 1, 16)
        self.mini_left_arrow = QtWidgets.QPushButton(Form)
        self.mini_left_arrow.setMaximumSize(QtCore.QSize(30, 30))
        self.mini_left_arrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mini_left_arrow.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/icon_left_mini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mini_left_arrow.setIcon(icon7)
        self.mini_left_arrow.setIconSize(QtCore.QSize(30, 30))
        self.mini_left_arrow.setFlat(True)
        self.mini_left_arrow.setObjectName("mini_left_arrow")
        self.gridLayout.addWidget(self.mini_left_arrow, 13, 0, 1, 1)
        self.mini_right_arrow = QtWidgets.QPushButton(Form)
        self.mini_right_arrow.setMaximumSize(QtCore.QSize(30, 30))
        self.mini_right_arrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mini_right_arrow.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/icon_right_mini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mini_right_arrow.setIcon(icon8)
        self.mini_right_arrow.setIconSize(QtCore.QSize(30, 30))
        self.mini_right_arrow.setFlat(True)
        self.mini_right_arrow.setObjectName("mini_right_arrow")
        self.gridLayout.addWidget(self.mini_right_arrow, 13, 15, 1, 1)
        self.widget_6 = QtWidgets.QWidget(Form)
        self.widget_6.setMinimumSize(QtCore.QSize(50, 120))
        self.widget_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mini_image_1 = QtWidgets.QLabel(self.widget_6)
        self.mini_image_1.setMinimumSize(QtCore.QSize(100, 50))
        self.mini_image_1.setMaximumSize(QtCore.QSize(150, 100))
        self.mini_image_1.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.mini_image_1.setAutoFillBackground(False)
        self.mini_image_1.setText("")
        self.mini_image_1.setScaledContents(False)
        self.mini_image_1.setObjectName("mini_image_1")
        self.horizontalLayout_2.addWidget(self.mini_image_1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.mini_image_2 = QtWidgets.QLabel(self.widget_6)
        self.mini_image_2.setMinimumSize(QtCore.QSize(100, 50))
        self.mini_image_2.setMaximumSize(QtCore.QSize(150, 100))
        self.mini_image_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.mini_image_2.setText("")
        self.mini_image_2.setScaledContents(False)
        self.mini_image_2.setObjectName("mini_image_2")
        self.horizontalLayout_2.addWidget(self.mini_image_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.mini_image_3 = QtWidgets.QLabel(self.widget_6)
        self.mini_image_3.setMinimumSize(QtCore.QSize(100, 50))
        self.mini_image_3.setMaximumSize(QtCore.QSize(150, 100))
        self.mini_image_3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.mini_image_3.setText("")
        self.mini_image_3.setScaledContents(False)
        self.mini_image_3.setObjectName("mini_image_3")
        self.horizontalLayout_2.addWidget(self.mini_image_3)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.mini_image_4 = QtWidgets.QLabel(self.widget_6)
        self.mini_image_4.setMinimumSize(QtCore.QSize(100, 50))
        self.mini_image_4.setMaximumSize(QtCore.QSize(150, 100))
        self.mini_image_4.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.mini_image_4.setText("")
        self.mini_image_4.setScaledContents(False)
        self.mini_image_4.setObjectName("mini_image_4")
        self.horizontalLayout_2.addWidget(self.mini_image_4)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.mini_image_5 = QtWidgets.QLabel(self.widget_6)
        self.mini_image_5.setMinimumSize(QtCore.QSize(100, 50))
        self.mini_image_5.setMaximumSize(QtCore.QSize(150, 100))
        self.mini_image_5.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.mini_image_5.setText("")
        self.mini_image_5.setScaledContents(False)
        self.mini_image_5.setObjectName("mini_image_5")
        self.horizontalLayout_2.addWidget(self.mini_image_5)
        self.gridLayout.addWidget(self.widget_6, 12, 1, 3, 14)
        self.main_image = QtWidgets.QLabel(Form)
        self.main_image.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_image.sizePolicy().hasHeightForWidth())
        self.main_image.setSizePolicy(sizePolicy)
        self.main_image.setMinimumSize(QtCore.QSize(0, 0))
        self.main_image.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.main_image.setText("")
        self.main_image.setScaledContents(False)
        self.main_image.setObjectName("main_image")
        self.gridLayout.addWidget(self.main_image, 0, 1, 9, 14)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Галерея"))
        self.map_button.setText(_translate("Form", "Карта"))
        self.result_button.setText(_translate("Form", "Результаты"))
        self.count_button.setText(_translate("Form", "Расчет"))
        self.all_button.setText(_translate("Form", "Карта все"))
        self.allcount_button.setText(_translate("Form", "Расчет для всех"))
