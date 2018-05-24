from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MouseAction(QAction):
    focusIn = pyqtSignal()
    focusOut = pyqtSignal()
    
    def focusInEvent(self, event):
        self.focusIn.emit()

    def focusOutEvent(self, event):
        self.focusOut.emit()
