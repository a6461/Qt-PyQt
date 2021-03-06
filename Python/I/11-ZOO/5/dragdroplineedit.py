from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dragdroplabel import *

class DragDropLineEdit(QLineEdit):
    tag = -1

    def dragEnterEvent(self, event):
        event.accept()
        self.setStyleSheet('background-color: yellow;')

    def dropEvent(self, event):
        src = event.source()
        if src.tag >= self.tag:
            self.setText(src.text())
            self.tag = src.tag
        src.setVisible(False)
        self.setStyleSheet('background-color: #f0f0f0;')

    def dragLeaveEvent(self, event):
        self.setStyleSheet('background-color: #f0f0f0;')
