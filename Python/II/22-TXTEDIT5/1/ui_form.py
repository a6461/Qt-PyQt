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
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        self.menuColors = QtWidgets.QMenu(self.menuFormat)
        self.menuColors.setObjectName("menuColors")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        Form.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolBar.setFont(font)
        self.toolBar.setObjectName("toolBar")
        Form.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(Form)
        self.statusBar.setStyleSheet("QStatusBar::item { border: none; };")
        self.statusBar.setObjectName("statusBar")
        Form.setStatusBar(self.statusBar)
        self.actionNew = QtWidgets.QAction(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(Form)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionExit = QtWidgets.QAction(Form)
        self.actionExit.setObjectName("actionExit")
        self.actionBold = QtWidgets.QAction(Form)
        self.actionBold.setCheckable(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionBold.setFont(font)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtWidgets.QAction(Form)
        self.actionItalic.setCheckable(True)
        font = QtGui.QFont()
        font.setItalic(True)
        self.actionItalic.setFont(font)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtWidgets.QAction(Form)
        self.actionUnderline.setCheckable(True)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.actionUnderline.setFont(font)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionStrikeOut = QtWidgets.QAction(Form)
        self.actionStrikeOut.setCheckable(True)
        font = QtGui.QFont()
        font.setStrikeOut(True)
        self.actionStrikeOut.setFont(font)
        self.actionStrikeOut.setObjectName("actionStrikeOut")
        self.actionLeft = QtWidgets.QAction(Form)
        self.actionLeft.setCheckable(True)
        self.actionLeft.setChecked(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLeft.setIcon(icon3)
        self.actionLeft.setObjectName("actionLeft")
        self.actionCenter = QtWidgets.QAction(Form)
        self.actionCenter.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCenter.setIcon(icon4)
        self.actionCenter.setObjectName("actionCenter")
        self.actionRight = QtWidgets.QAction(Form)
        self.actionRight.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRight.setIcon(icon5)
        self.actionRight.setObjectName("actionRight")
        self.actionJustify = QtWidgets.QAction(Form)
        self.actionJustify.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/justify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJustify.setIcon(icon6)
        self.actionJustify.setObjectName("actionJustify")
        self.actionFontColor = QtWidgets.QAction(Form)
        self.actionFontColor.setObjectName("actionFontColor")
        self.actionBackgroundColor = QtWidgets.QAction(Form)
        self.actionBackgroundColor.setObjectName("actionBackgroundColor")
        self.actionFont = QtWidgets.QAction(Form)
        self.actionFont.setObjectName("actionFont")
        self.actionUndo = QtWidgets.QAction(Form)
        self.actionUndo.setObjectName("actionUndo")
        self.actionCut = QtWidgets.QAction(Form)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon7)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(Form)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon8)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(Form)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon9)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(Form)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelectAll = QtWidgets.QAction(Form)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuColors.addAction(self.actionFontColor)
        self.menuColors.addAction(self.actionBackgroundColor)
        self.menuFormat.addAction(self.actionBold)
        self.menuFormat.addAction(self.actionItalic)
        self.menuFormat.addAction(self.actionUnderline)
        self.menuFormat.addAction(self.actionStrikeOut)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionLeft)
        self.menuFormat.addAction(self.actionCenter)
        self.menuFormat.addAction(self.actionRight)
        self.menuFormat.addAction(self.actionJustify)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.menuColors.menuAction())
        self.menuFormat.addAction(self.actionFont)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelectAll)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBold)
        self.toolBar.addAction(self.actionItalic)
        self.toolBar.addAction(self.actionUnderline)
        self.toolBar.addAction(self.actionStrikeOut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLeft)
        self.toolBar.addAction(self.actionCenter)
        self.toolBar.addAction(self.actionRight)
        self.toolBar.addAction(self.actionJustify)

        self.retranslateUi(Form)
        self.actionExit.triggered.connect(Form.close)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionSelectAll.triggered.connect(self.textEdit.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Text Editor"))
        self.menuFile.setTitle(_translate("Form", "&File"))
        self.menuFormat.setTitle(_translate("Form", "F&ormat"))
        self.menuColors.setTitle(_translate("Form", "&Colors"))
        self.menuEdit.setTitle(_translate("Form", "&Edit"))
        self.toolBar.setWindowTitle(_translate("Form", "toolBar"))
        self.actionNew.setText(_translate("Form", "&New"))
        self.actionNew.setShortcut(_translate("Form", "Ctrl+N"))
        self.actionOpen.setText(_translate("Form", "&Open"))
        self.actionOpen.setShortcut(_translate("Form", "Ctrl+O"))
        self.actionSave.setText(_translate("Form", "&Save"))
        self.actionSave.setShortcut(_translate("Form", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("Form", "Save &As"))
        self.actionSaveAs.setShortcut(_translate("Form", "F12"))
        self.actionExit.setText(_translate("Form", "E&xit"))
        self.actionBold.setText(_translate("Form", "&Bold"))
        self.actionBold.setIconText(_translate("Form", "B"))
        self.actionBold.setShortcut(_translate("Form", "Ctrl+B"))
        self.actionItalic.setText(_translate("Form", "&Italic"))
        self.actionItalic.setIconText(_translate("Form", "I"))
        self.actionItalic.setShortcut(_translate("Form", "Ctrl+I"))
        self.actionUnderline.setText(_translate("Form", "&Underline"))
        self.actionUnderline.setIconText(_translate("Form", "U"))
        self.actionUnderline.setShortcut(_translate("Form", "Ctrl+U"))
        self.actionStrikeOut.setText(_translate("Form", "S&trikeout"))
        self.actionStrikeOut.setIconText(_translate("Form", "S"))
        self.actionStrikeOut.setShortcut(_translate("Form", "Ctrl+T"))
        self.actionLeft.setText(_translate("Form", "&Left alignment"))
        self.actionLeft.setIconText(_translate("Form", "Left alignment"))
        self.actionLeft.setShortcut(_translate("Form", "Ctrl+L"))
        self.actionCenter.setText(_translate("Form", "C&enter"))
        self.actionCenter.setIconText(_translate("Form", "Center"))
        self.actionCenter.setShortcut(_translate("Form", "Ctrl+E"))
        self.actionRight.setText(_translate("Form", "&Right alignment"))
        self.actionRight.setIconText(_translate("Form", "Right alignment"))
        self.actionRight.setShortcut(_translate("Form", "Ctrl+R"))
        self.actionJustify.setText(_translate("Form", "&Justify"))
        self.actionJustify.setShortcut(_translate("Form", "Ctrl+J"))
        self.actionFontColor.setText(_translate("Form", "&Font color..."))
        self.actionBackgroundColor.setText(_translate("Form", "&Background color..."))
        self.actionFont.setText(_translate("Form", "&Font..."))
        self.actionUndo.setText(_translate("Form", "&Undo"))
        self.actionUndo.setShortcut(_translate("Form", "Ctrl+Z"))
        self.actionCut.setText(_translate("Form", "Cu&t"))
        self.actionCut.setShortcut(_translate("Form", "Ctrl+X"))
        self.actionCopy.setText(_translate("Form", "&Copy"))
        self.actionCopy.setShortcut(_translate("Form", "Ctrl+C"))
        self.actionPaste.setText(_translate("Form", "&Paste"))
        self.actionPaste.setShortcut(_translate("Form", "Ctrl+V"))
        self.actionDelete.setText(_translate("Form", "&Delete"))
        self.actionSelectAll.setText(_translate("Form", "&Select All"))
        self.actionSelectAll.setShortcut(_translate("Form", "Ctrl+A"))

import icons_rc
