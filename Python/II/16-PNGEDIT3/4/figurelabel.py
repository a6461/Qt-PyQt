from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FigureLabel(QLabel):
    mousePressed = pyqtSignal()
    painted = pyqtSignal()

    def mousePressEvent(self, event):
        self.mousePressed.emit()

    def paintEvent(self, event):
        self.painted.emit()
