from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropLineEdit(QLineEdit):
    tag = -1
    
    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        src = event.source()
        if src.tag >= self.tag:
            self.setText(src.text())
            self.tag = src.tag
        src.setVisible(False)
