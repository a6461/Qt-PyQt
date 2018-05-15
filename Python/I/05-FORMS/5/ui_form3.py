# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(417, 125)
        Form3.setModal(True)
        self.formLayoutWidget = QtWidgets.QWidget(Form3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(26)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form3)
        self.buttonBox.setGeometry(QtCore.QRect(170, 90, 231, 23))
        self.buttonBox.setStyleSheet("button-layout: 2;")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Form3)
        self.buttonBox.accepted.connect(Form3.accept)
        self.buttonBox.rejected.connect(Form3.reject)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Диалоговое окно"))
        self.label.setText(_translate("Form3", "Заголовок главного окна:"))
        self.label_2.setText(_translate("Form3", "Заголовок подчиненного окна:"))
        self.lineEdit.setText(_translate("Form3", "Главное окно"))
        self.lineEdit_2.setText(_translate("Form3", "Подчиненное окно"))

