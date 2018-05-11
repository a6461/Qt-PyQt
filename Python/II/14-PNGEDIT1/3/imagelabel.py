from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ImageLabel(QLabel):
    mouseMoved = pyqtSignal(QMouseEvent)
    mousePressed = pyqtSignal(QMouseEvent)
    
    def mouseMoveEvent(self, event):
        self.mouseMoved.emit(event)

    def mousePressEvent(self, event):
        self.mousePressed.emit(event)
