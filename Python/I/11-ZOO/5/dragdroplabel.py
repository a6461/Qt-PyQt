from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropLabel(QLabel):
    tag = -1
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.setStyleSheet('color: blue;')
            drag = QDrag(self)
            drag.setMimeData(QMimeData())
            drag.exec()
            rect = self.parent().rect()
            pos = self.parent().mapFromGlobal(QCursor.pos())
            if not rect.contains(pos):
                self.setVisible(False)
            self.setStyleSheet('color: black;')

    def dragEnterEvent(self, event):
        event.accept()
        self.setStyleSheet(
            self.styleSheet() + 'background-color: yellow;')
        
    def dropEvent(self, event):
        src = event.source()
        if self == src:
            return
        if src.tag > self.tag:
            src.move(self.pos())
            self.setVisible(False)
        else:
            src.setVisible(False)

    def dragLeaveEvent(self, event):
        self.setStyleSheet(
            self.styleSheet() + 'background-color: #f0f0f0;')
