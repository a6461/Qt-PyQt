from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CursorButton(QPushButton):
    mousePressed = pyqtSignal(QMouseEvent)
    
    def mousePressEvent(self, event):
        self.mousePressed.emit(event)
