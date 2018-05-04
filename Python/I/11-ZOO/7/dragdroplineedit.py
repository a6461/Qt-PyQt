from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dragdroplabel import *

class DragDropLineEdit(QLineEdit):
    tag = -1

    def dragEnterEvent(self, event):
        event.accept()
        self.setStyleSheet('background-color: yellow;')

    def dragLeaveEvent(self, event):
        self.setStyleSheet('background-color: #F0F0F0;')

    def dropEvent(self, event):
        lb = event.source()
        if lb.tag >= self.tag:
            self.setText(lb.text())
            self.tag = lb.tag
        lb.setVisible(False)
        self.setStyleSheet('background-color: #F0F0F0;')
