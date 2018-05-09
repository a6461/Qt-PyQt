from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WildButton(QPushButton):
    mouseMoved = pyqtSignal()
    
    def mouseMoveEvent(self, event):
        self.mouseMoved.emit()
        
