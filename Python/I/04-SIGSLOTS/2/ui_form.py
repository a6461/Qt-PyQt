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
        Form.resize(292, 140)
        self.button = QtWidgets.QPushButton(Form)
        self.button.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.button.setObjectName("button")
        self.button_2 = WildButton(Form)
        self.button_2.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.button_2.setMouseTracking(True)
        self.button_2.setText("")
        self.button_2.setObjectName("button_2")

        self.retranslateUi(Form)
        self.button.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Прыгающие кнопки"))
        self.button.setText(_translate("Form", "Закрыть"))

from wildbutton import WildButton
