from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class DragDropGroupBox(QGroupBox):
    def __init__(self, parent = None):
        super(self.__class__, self).__init__(parent)
        
    def dragEnterEvent(self, event):
        event.acceptProposedAction()
    
    def dropEvent(self, event):
        k = sys.maxsize
        if len(self.children()) > 0:
            k = self.children()[len(self.children()) - 1].width()
        lb = event.source()
        if k > lb.width():
            lb.setParent(self)
            lb.move((self.width() - lb.width()) / 2,
                    self.height() - 2 - len(self.children()) * lb.height())
            lb.show()
