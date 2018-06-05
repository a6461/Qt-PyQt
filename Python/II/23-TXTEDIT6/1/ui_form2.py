# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(357, 163)
        self.groupBox = QtWidgets.QGroupBox(Form2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 192, 100))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 171, 74))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form2)
        self.buttonBox.setGeometry(QtCore.QRect(190, 130, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox = QtWidgets.QCheckBox(Form2)
        self.checkBox.setGeometry(QtCore.QRect(223, 81, 101, 17))
        self.checkBox.setObjectName("checkBox")
        self.label_4 = QtWidgets.QLabel(Form2)
        self.label_4.setGeometry(QtCore.QRect(223, 10, 85, 13))
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(Form2)
        self.comboBox_4.setGeometry(QtCore.QRect(223, 33, 121, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Абзац"))
        self.groupBox.setTitle(_translate("Form2", "Отступы"))
        self.label.setText(_translate("Form2", "От левого края:"))
        self.label_2.setText(_translate("Form2", "От правого края:"))
        self.label_3.setText(_translate("Form2", "От метки:"))
        self.checkBox.setText(_translate("Form2", "Абзац с меткой"))
        self.label_4.setText(_translate("Form2", "Выравнивание:"))
        self.comboBox_4.setItemText(0, _translate("Form2", "По левому краю"))
        self.comboBox_4.setItemText(1, _translate("Form2", "По центру"))
        self.comboBox_4.setItemText(2, _translate("Form2", "По правому краю"))
        self.comboBox_4.setItemText(3, _translate("Form2", "По ширине"))

