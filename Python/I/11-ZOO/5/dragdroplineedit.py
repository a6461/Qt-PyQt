from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dragdroplabel import *

class DragDropLineEdit(QLineEdit):
    tag = -1

    def dragEnterEvent(self, event):
        event.accept()
        palette = self.palette()
        palette.setColor(QPalette.Base, Qt.yellow)
        self.setPalette(palette)

    def dragLeaveEvent(self, event):
        palette = self.palette()
        palette.setColor(QPalette.Base, QColor('#F0F0F0'))
        self.setPalette(palette)

    def dropEvent(self, event):
        lb = event.source()
        if lb.tag >= self.tag:
            self.setText(lb.text())
            self.tag = lb.tag
        lb.setVisible(False)
        palette = self.palette()
        palette.setColor(QPalette.Base, QColor('#F0F0F0'))
        self.setPalette(palette)
