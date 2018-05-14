from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropLabel(QLabel):
    tag = -1
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            drag.setMimeData(QMimeData())
            drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        src = event.source()
        if self == src:
            return
        if src.tag > self.tag:
            src.move(self.pos())
            self.setVisible(False)
        else:
            src.setVisible(False)
