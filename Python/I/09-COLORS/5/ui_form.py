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
        Form.resize(292, 335)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(3, 3, -1, -1)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setProperty("value", 255)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(32)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider)
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_2.setTickInterval(32)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_2)
        self.horizontalSlider_3 = QtWidgets.QSlider(Form)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_3.setTickInterval(32)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_3)
        self.horizontalSlider_4 = QtWidgets.QSlider(Form)
        self.horizontalSlider_4.setMaximum(255)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_4.setTickInterval(32)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_4)
        self.horizontalSlider_5 = QtWidgets.QSlider(Form)
        self.horizontalSlider_5.setMaximum(255)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_5.setTickInterval(32)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_5)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("background-color: black; color: white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Colors"))
        self.label.setText(_translate("Form", "Alpha"))
        self.label_2.setText(_translate("Form", "Red"))
        self.label_3.setText(_translate("Form", "Green"))
        self.label_4.setText(_translate("Form", "Blue"))
        self.label_5.setText(_translate("Form", "Gray"))
        self.label_6.setText(_translate("Form", "Color"))

