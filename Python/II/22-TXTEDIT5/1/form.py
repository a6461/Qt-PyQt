from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, win32api, win32con

class Form(Ui_Form, QMainWindow):
    savePath = ''
    openPath = ''
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.actionExit.setShortcut('Alt+F4')
        self.actionItalic.triggered.connect(self.on_actionBold_triggered)
        self.actionUnderline.triggered.connect(self.on_actionBold_triggered)
        self.actionStrikeOut.triggered.connect(self.on_actionBold_triggered)
        self.alignGroup = QActionGroup(self)
        self.alignGroup.addAction(self.actionLeft)
        self.actionLeft.setProperty('tag', Qt.AlignLeft)
        self.alignGroup.addAction(self.actionCenter)
        self.actionCenter.setProperty('tag', Qt.AlignHCenter)
        self.alignGroup.addAction(self.actionRight)
        self.actionRight.setProperty('tag', Qt.AlignRight)
        self.alignGroup.addAction(self.actionJustify)
        self.actionJustify.setProperty('tag', Qt.AlignJustify)
        self.alignGroup.triggered.connect(self.setAlignment)
        self.contextMenu = QMenu()
        self.contextMenu.addAction(self.actionCut)
        self.contextMenu.addAction(self.actionCopy)
        self.contextMenu.addAction(self.actionPaste)
        self.contextMenu.addAction(self.actionFont)
        self.contextMenu.insertSeparator(self.contextMenu.actions()[3])
        self.textEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.textEdit.customContextMenuRequested.connect(self.contextMenuShow)
        self.cap = QLabel('CAP')
        self.cap.setFrameShape(QFrame.WinPanel)
        self.cap.setFrameShadow(QFrame.Sunken)
        self.cap.setFixedWidth(40)
        self.cap.setAlignment(Qt.AlignHCenter)
        self.num = QLabel('NUM')
        self.num.setFrameShape(QFrame.WinPanel)
        self.num.setFrameShadow(QFrame.Sunken)
        self.num.setFixedWidth(40)
        self.num.setAlignment(Qt.AlignHCenter)
        self.modified = QLabel('Modified')
        self.modified.setFrameShape(QFrame.WinPanel)
        self.modified.setFrameShadow(QFrame.Sunken)
        self.modified.setFixedWidth(60)
        self.modified.setAlignment(Qt.AlignHCenter)
        self.hint = QLabel('Ready')
        self.statusBar.addWidget(self.cap)
        self.statusBar.addWidget(self.num)
        self.statusBar.addWidget(self.modified)
        self.statusBar.addWidget(self.hint)
        self.timer = QTimer(self)
        self.timer.start(200)
        self.timer.timeout.connect(self.tick)
        self.tick()

    def saveToFile(self, path):
        with open(path, 'w') as file:
            file.write(self.textEdit.toPlainText())
        self.textEdit.document().setModified(False)

    @pyqtSlot()
    def on_actionSaveAs_triggered(self):
        self.savePath = QFileDialog.getSaveFileName(self, 'Сохранение файла',
                                    '', 'Text files (*.txt)')[0]
        if self.savePath:
            self.saveToFile(self.savePath)
            self.setWindowTitle('Text Editor - '
                                + os.path.basename(self.savePath))

    @pyqtSlot()
    def on_actionSave_triggered(self):
        if not self.savePath:
            self.on_actionSaveAs_triggered()
        else:
            self.saveToFile(self.savePath)

    @pyqtSlot()
    def on_actionNew_triggered(self):
        if self.textSaved():
            self.textEdit.clear()
            self.setWindowTitle('Text Editor')
            self.savePath = ''

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        if self.textSaved():
            self.openPath = QFileDialog.getOpenFileName(self, 'Открытие файла',
                                    '', 'Text files (*.txt)')[0]
            if self.openPath:
                with open(self.openPath, 'r') as file:
                    self.textEdit.setText(file.read())
                self.setWindowTitle('Text Editor - '
                                + os.path.basename(self.openPath))
                self.savePath = self.openPath
                self.openPath = ''

    def textSaved(self):
        if self.textEdit.document().isModified():
            question = QMessageBox.question(self, "Подтверждение", 
                     "Сохранить изменения в документе?", QMessageBox.Yes |
                        QMessageBox.No | QMessageBox.Cancel)
            if question == QMessageBox.Yes:
                self.on_actionSave_triggered()
                return not self.textEdit.document().isModified()
            elif question == QMessageBox.Cancel:
                return False
        return True

    def closeEvent(self, event):
        if not self.textSaved():
            event.ignore()

    @pyqtSlot()
    def on_actionBold_triggered(self):
        a = self.sender()
        a.setChecked(a.isChecked())
        tc = self.textEdit.textCursor()
        cf = tc.charFormat()
        cf.setFontWeight(
            QFont.Bold if self.actionBold.isChecked() else QFont.Normal)
        cf.setFontItalic(self.actionItalic.isChecked())
        cf.setFontUnderline(self.actionUnderline.isChecked())
        cf.setFontStrikeOut(self.actionStrikeOut.isChecked())
        tc.setCharFormat(cf)
        self.textEdit.setTextCursor(tc)

    @pyqtSlot()
    def on_textEdit_selectionChanged(self):
        tc = self.textEdit.textCursor()
        cf = tc.charFormat() 
        self.actionBold.setChecked(cf.font().bold())
        self.actionItalic.setChecked(cf.font().italic())
        self.actionUnderline.setChecked(cf.font().underline())
        self.actionStrikeOut.setChecked(cf.font().strikeOut())
        bf = tc.blockFormat()
        if bf.alignment() == Qt.AlignLeft:
            self.actionLeft.setChecked(True)
        elif bf.alignment() == Qt.AlignCenter:
            self.actionCenter.setChecked(True)
        elif bf.alignment() == Qt.AlignRight:
            self.actionRight.setChecked(True)
        else:
            self.actionJustify.setChecked(True)

    def setAlignment(self, action):
        if not action.isChecked():
            return
        tc = self.textEdit.textCursor()
        bf = tc.blockFormat()
        bf.setAlignment(Qt.AlignmentFlag(action.property('tag')))
        tc.setBlockFormat(bf)
        self.textEdit.setTextCursor(tc)

    @pyqtSlot()
    def on_actionFontColor_triggered(self):
        tc = self.textEdit.textCursor()
        cf = tc.charFormat()
        color = QColorDialog.getColor(
            cf.foreground().color())    
        if not color.isValid():
            return
        cf.setForeground(QBrush(color))
        tc.setCharFormat(cf)
        self.textEdit.setTextCursor(tc)

    @pyqtSlot()
    def on_actionBackgroundColor_triggered(self):
        tc = self.textEdit.textCursor()
        cf = tc.charFormat()
        color = QColorDialog.getColor(
            cf.background().color())     
        if not color.isValid():
            return
        cf.setBackground(QBrush(color))
        tc.setCharFormat(cf)
        self.textEdit.setTextCursor(tc)

    @pyqtSlot()
    def on_actionFont_triggered(self):
        tc = self.textEdit.textCursor()
        cf = tc.charFormat()
        font, ok = QFontDialog.getFont(cf.font())
        if ok:
            cf.setFont(font)
            self.actionBold.setChecked(font.bold())
            self.actionItalic.setChecked(font.italic())
            self.actionUnderline.setChecked(font.underline())
            self.actionStrikeOut.setChecked(font.strikeOut())
        tc.setCharFormat(cf)
        self.textEdit.setTextCursor(tc)

    @pyqtSlot()
    def on_actionDelete_triggered(self):
        self.textEdit.textCursor().removeSelectedText()

    @pyqtSlot()
    def on_menuEdit_aboutToShow(self):
        self.actionUndo.setEnabled(self.textEdit.document().isUndoAvailable())
        isNotEmpty = len(self.textEdit.textCursor().selectedText()) > 0
        self.actionCut.setEnabled(isNotEmpty)
        self.actionCopy.setEnabled(isNotEmpty)
        self.actionDelete.setEnabled(isNotEmpty)
        self.actionPaste.setEnabled(self.textEdit.canPaste())
        self.actionSelectAll.setEnabled(self.textEdit.toPlainText() != '')

    def contextMenuShow(self, pos):
        isNotEmpty = len(self.textEdit.textCursor().selectedText()) > 0
        self.contextMenu.actions()[0].setEnabled(isNotEmpty)
        self.contextMenu.actions()[1].setEnabled(isNotEmpty)
        self.contextMenu.actions()[2].setEnabled(self.textEdit.canPaste())
        self.contextMenu.exec(self.mapToGlobal(pos))

    def tick(self):
        self.cap.setText('CAP' if self.isCapsLock() else '')
        self.num.setText('NUM' if self.isNumLock() else '')
        self.modified.setText(
            'Modified' if self.textEdit.document().isModified() else '')

    def isCapsLock(self):
        if os.name == 'nt':
            return win32api.GetKeyState(win32con.VK_CAPITAL) == 1
        
    def isNumLock(self):
        if os.name == 'nt':
            return win32api.GetKeyState(win32con.VK_NUMLOCK) == 1
