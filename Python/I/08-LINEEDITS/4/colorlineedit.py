from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ColorLineEdit(QLineEdit):
    def __init__(self, parent = None):
        super(self.__class__, self).__init__(parent)
        self.textChanged.connect(self.otextChanged)
        action = QAction(QIcon(self.style().standardPixmap(
            QStyle.SP_MessageBoxCritical)), '')
        self.addAction(action, QLineEdit.TrailingPosition)
    
    def focusInEvent(self, event):
        self.setStyleSheet('background-color: darkGreen; color: white')
        self.selectAll()
        QApplication.sendEvent(self,
            QKeyEvent(QEvent.KeyPress, Qt.Key_Right, Qt.NoModifier))
        self.deselect()

    def focusOutEvent(self, event):
        self.selectAll()
        self.deselect()
        self.setStyleSheet('background-color: Window; color: WindowText')
        if self.text() == '':
            self.setFocus()

    def otextChanged(self):
        if len(self.actions()) > 0:
            self.removeAction(self.actions()[0])
        if self.text().strip() == '':
            if len(self.actions()) == 0:
                action = QAction(
                    QIcon(self.style().standardPixmap(
                        QStyle.SP_MessageBoxCritical)), '', self)
                self.addAction(action, QLineEdit.TrailingPosition)
