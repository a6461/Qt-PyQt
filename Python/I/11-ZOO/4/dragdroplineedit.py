from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropLineEdit(QLineEdit):
    tag = -1
    
    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        lb = event.source()
        if lb.tag >= self.tag:
            self.setText(lb.text())
            self.tag = lb.tag
        lb.setVisible(False)
