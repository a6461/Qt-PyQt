from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropPushButton(QPushButton):
    def dragEnterEvent(self, event):
        self.parent().dragEnterEvent(event)
