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
        self.label.setGeometry(QtCore.QRect(20, 42, 52, 13))
        self.label.setObjectName("label")
        self.label_2 = DragDropLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(127, 42, 32, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = DragDropLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(233, 42, 45, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = DragDropLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(340, 42, 32, 13))
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 421, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = DragDropLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet("background-color: #f0f0f0;")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = DragDropLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setStyleSheet("background-color: #f0f0f0;")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = DragDropLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setStyleSheet("background-color: #f0f0f0;")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = DragDropLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setStyleSheet("background-color: #f0f0f0;")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)

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
from dragdroplineedit import DragDropLineEdit
