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
        Form.resize(250, 127)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(16)
        self.formLayout.setObjectName("formLayout")
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.checkBox_2 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_2)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(91, 92, 147, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CheckBoxes"))
        self.checkBox.setText(_translate("Form", "Группа 1"))
        self.label.setText(_translate("Form", "Пункты не выбраны"))
        self.checkBox_2.setText(_translate("Form", "Группа 2"))
        self.label_2.setText(_translate("Form", "Пункты не выбраны"))
        self.checkBox_3.setText(_translate("Form", "Группа 3"))
        self.label_3.setText(_translate("Form", "Пункты не выбраны"))
        self.pushButton.setText(_translate("Form", "Выбор пунктов"))

