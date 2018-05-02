from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropLabel(QLabel):
    tag = -1
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            palette = self.palette()
            palette.setColor(QPalette.Foreground, Qt.blue)
            self.setPalette(palette)
            drag = QDrag(self)
            drag.setMimeData(QMimeData())
            drag.exec()
            rect = self.parent().rect()
            pos = self.parent().mapFromGlobal(QCursor.pos())
            if not rect.contains(pos):
                self.setVisible(False)
            palette.setColor(QPalette.Foreground, Qt.black)
            self.setPalette(palette)
            s = ''
            for child in self.parent().children():
                if child.objectName()[0] == 'l':
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
        palette = self.palette()
        palette.setColor(QPalette.Background, Qt.yellow)
        self.setPalette(palette)
        
    def dropEvent(self, event):
        lb = event.source()
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor('#F0F0F0'))
        self.setPalette(palette)
        if self == lb:
            return
        if lb.tag > self.tag:
            lb.move(self.pos())
            self.setVisible(False)
        else:
            lb.setVisible(False)

    def dragLeaveEvent(self, event):
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor('#F0F0F0'))
        self.setPalette(palette)
