# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(452, 245)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(10, 10, 42, 22))
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(10)
        self.spinBox.setProperty("value", 4)
        self.spinBox.setObjectName("spinBox")
        self.groupBox_2 = DragDropGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(156, 41, 139, 189))
        self.groupBox_2.setAcceptDrops(True)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox = DragDropGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(11, 41, 139, 189))
        self.groupBox.setAcceptDrops(True)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_3 = DragDropGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(301, 41, 139, 189))
        self.groupBox_3.setAcceptDrops(True)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(297, 10, 47, 13))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ханойские башни"))
        self.groupBox_2.setTitle(_translate("Form", "Промежуточная позиция"))
        self.groupBox.setTitle(_translate("Form", "Начальная позиция"))
        self.groupBox_3.setTitle(_translate("Form", "Конечная позиция"))
        self.pushButton.setText(_translate("Form", "Сброс"))
        self.label.setText(_translate("Form", "TextLabel"))

from dragdropgroupbox import DragDropGroupBox
