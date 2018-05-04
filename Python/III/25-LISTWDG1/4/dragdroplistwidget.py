from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragDropListWidget(QListWidget):
    iSrc = -1

    def mouseDoubleClickEvent(self, event):
        self.parent().on_label_2_clicked()
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.RightButton:
            self.iSrc = self.row(self.itemAt(event.pos()))
            if self.iSrc != -1:
                drag = QDrag(self)
                mimeData = QMimeData()
                mimeData.setText(self.item(self.iSrc).text())
                drag.setMimeData(mimeData)
                drag.exec_(Qt.MoveAction)
        else:
            self.setCurrentRow(self.row(self.itemAt(event.pos())))

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if event.dropAction() == Qt.MoveAction:
            self.takeItem(self.iSrc)
        s = event.mimeData().text()
        iTrg = self.row(self.itemAt(event.pos()))
        if iTrg == -1:
            self.addItem(s)
            self.item(self.count() - 1).setSelected(True)
            self.setCurrentRow(self.count() - 1)
        else:
            self.insertItem(iTrg, s)
            self.setCurrentRow(iTrg)
