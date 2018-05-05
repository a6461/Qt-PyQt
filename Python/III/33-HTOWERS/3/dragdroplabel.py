from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropLabel(QLabel):
    def __init__(self, parent = None):
        super(self.__class__, self).__init__(parent)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            index = self.parent().children().index(self)
            drag = QDrag(self)
            drag.setMimeData(QMimeData())            
            if index == len(self.parent().children()) - 1:
                drag.exec_(Qt.MoveAction)
            else:
                drag.exec_(Qt.IgnoreAction)
