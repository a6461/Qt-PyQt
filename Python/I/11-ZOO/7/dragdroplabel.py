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
            s = ''
            for child in self.parent().children()[0:4]:
                if child.isVisible():
                    return
                s += child.text()
            if s == '':
                return
            self.parent().pushButton.setText('Зоопарк открыт')
            self.parent().pushButton.setStyleSheet('color: green;')
            self.parent().pushButton.setIcon(
                self.style().standardIcon(QStyle.SP_DialogApplyButton))

    def dragEnterEvent(self, event):
        event.accept()
        self.setStyleSheet(
            self.styleSheet() + 'background-color: yellow;')
        
    def dropEvent(self, event):
        lb = event.source()
        self.setStyleSheet(
            self.styleSheet() + 'background-color: #F0F0F0;')
        if self == lb:
            return
        if lb.tag > self.tag:
            lb.move(self.pos())
            self.setVisible(False)
        else:
            lb.setVisible(False)

    def dragLeaveEvent(self, event):
        self.setStyleSheet(
            self.styleSheet() + 'background-color: #F0F0F0;')

