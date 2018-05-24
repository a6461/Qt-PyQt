from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

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
        self.textEdit.setAlignment(Qt.AlignmentFlag(action.property('tag')))

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
