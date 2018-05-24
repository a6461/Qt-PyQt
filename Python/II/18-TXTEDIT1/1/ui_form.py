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
        Form.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        Form.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(Form)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(Form)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Form)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(Form)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionExit = QtWidgets.QAction(Form)
        self.actionExit.setObjectName("actionExit")
        self.menu_File.addAction(self.actionNew)
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionSaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(Form)
        self.actionExit.triggered.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Text Editor"))
        self.menu_File.setTitle(_translate("Form", "&File"))
        self.actionNew.setText(_translate("Form", "&New"))
        self.actionNew.setShortcut(_translate("Form", "Ctrl+N"))
        self.actionOpen.setText(_translate("Form", "&Open"))
        self.actionOpen.setShortcut(_translate("Form", "Ctrl+O"))
        self.actionSave.setText(_translate("Form", "&Save"))
        self.actionSave.setShortcut(_translate("Form", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("Form", "Save &As"))
        self.actionSaveAs.setShortcut(_translate("Form", "F12"))
        self.actionExit.setText(_translate("Form", "E&xit"))

