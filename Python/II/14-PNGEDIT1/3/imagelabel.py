from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ImageLabel(QLabel):
    mouseMoved = pyqtSignal(QMouseEvent)
    startChanged = pyqtSignal(QPoint)
    
    def mouseMoveEvent(self, event):
        self.mouseMoved.emit(event)

    def mousePressEvent(self, event):
        self.startChanged.emit(event.pos())
