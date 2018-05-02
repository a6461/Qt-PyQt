from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        child = self.childAt(event.pos())
        if (child == None or child == event.source()):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        lb = event.source()
        lb.move(event.pos())
