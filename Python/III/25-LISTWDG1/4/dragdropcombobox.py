from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropComboBox(QComboBox):    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.RightButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            mimeData.setText(self.currentText())
            drag.setMimeData(mimeData)
            drag.exec_(Qt.CopyAction)
        else:
            self.showPopup()

    def dragEnterEvent(self, event):
        event.acceptProposedAction()
