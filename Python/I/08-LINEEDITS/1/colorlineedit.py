from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ColorLineEdit(QLineEdit):
    def focusInEvent(self, event):
        self.setStyleSheet('background-color: darkGreen; color: white')
        self.selectAll()
        QApplication.sendEvent(self,
            QKeyEvent(QEvent.KeyPress, Qt.Key_Right, Qt.NoModifier))
        self.deselect()

    def focusOutEvent(self, event):
        self.selectAll()
        self.deselect()
        self.setStyleSheet('background-color: Window; color: WindowText')
