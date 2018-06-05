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
        Form.resize(336, 184)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_3 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.lineEdit_4 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 0, 1, 1)
        self.lineEdit_5 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.lineEdit_6 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 1, 2, 1, 1)
        self.lineEdit_7 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 2, 0, 1, 1)
        self.lineEdit_8 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 2, 1, 1, 1)
        self.lineEdit_9 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 2, 2, 1, 1)
        self.lineEdit_10 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 3, 0, 1, 1)
        self.lineEdit_11 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 3, 1, 1, 1)
        self.lineEdit_12 = ColorLineEdit(self.gridLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 3, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LineEdits"))
        self.lineEdit.setText(_translate("Form", "Data"))
        self.lineEdit_2.setText(_translate("Form", "Data"))
        self.lineEdit_3.setText(_translate("Form", "Data"))
        self.lineEdit_4.setText(_translate("Form", "Data"))
        self.lineEdit_5.setText(_translate("Form", "Data"))
        self.lineEdit_6.setText(_translate("Form", "Data"))
        self.lineEdit_7.setText(_translate("Form", "Data"))
        self.lineEdit_8.setText(_translate("Form", "Data"))
        self.lineEdit_9.setText(_translate("Form", "Data"))
        self.lineEdit_10.setText(_translate("Form", "Data"))
        self.lineEdit_11.setText(_translate("Form", "Data"))
        self.lineEdit_12.setText(_translate("Form", "Data"))

from colorlineedit import ColorLineEdit
