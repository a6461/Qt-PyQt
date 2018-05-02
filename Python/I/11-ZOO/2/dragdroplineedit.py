from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropLineEdit(QLineEdit):
    def dragEnterEvent(self, event):
        if self.text() == '':
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        lb = event.source()
        self.setText(lb.text())
        lb.setVisible(False)
