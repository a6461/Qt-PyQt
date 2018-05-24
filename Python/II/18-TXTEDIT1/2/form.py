from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

class Form(Ui_Form, QMainWindow):
    savePath = ''
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.actionExit.setShortcut('Alt+F4')

    def saveToFile(self, path):
        with open(path, 'w') as file:
            file.write(self.textEdit.toPlainText())

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
