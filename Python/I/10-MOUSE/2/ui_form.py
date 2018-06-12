# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(424, 273)
        Form.setWidgetResizable(True)
        self.frame = MouseFrame()
        self.frame.setGeometry(QtCore.QRect(10, 10, 200, 100))
        self.frame.setMouseTracking(True)
        self.frame.setStyleSheet("background-color: red;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        Form.setWidget(self.frame)
        self.frame1 = MouseFrame()
        self.frame1.setGeometry(QtCore.QRect(10, 130, 200, 100))
        self.frame1.setMouseTracking(True)
        self.frame1.setStyleSheet("background-color: green;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame1.setObjectName("frame1")
        Form.setWidget(self.frame1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ScrollArea"))

from mouseframe import MouseFrame
