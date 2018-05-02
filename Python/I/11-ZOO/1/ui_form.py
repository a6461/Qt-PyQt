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
        Form.resize(463, 189)
        Form.setAcceptDrops(True)
        self.label = DragDropLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 39, 52, 13))
        self.label.setObjectName("label")
        self.label_2 = DragDropLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(126, 39, 32, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = DragDropLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(232, 39, 45, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = DragDropLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(338, 39, 32, 13))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Зоопарк"))
        self.label.setText(_translate("Form", "Медведь"))
        self.label_2.setText(_translate("Form", "Волк"))
        self.label_3.setText(_translate("Form", "Лисица"))
        self.label_4.setText(_translate("Form", "Заяц"))

from dragdroplabel import DragDropLabel
