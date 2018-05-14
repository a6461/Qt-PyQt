from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mouseframe import *

class Form(Ui_Form, QWidget):
    p = QPoint()
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.frame.mouseMoved.connect(self.frameMouseMove)
        self.frame_2.mouseMoved.connect(self.frameMouseMove)
        self.frame.mousePressed.connect(self.frameMousePress)
        self.frame_2.mousePressed.connect(self.frameMousePress)   

    def frameMouseMove(self, event):
        a = self.sender()
        self.setWindowTitle('Mouse - {} {{X={},Y={}}}'.format(
            a.objectName(), a.x(), a.y()))
        if event.buttons() == Qt.LeftButton:
            a.move(a.pos() + event.pos() - self.p)

    def frameMousePress(self, event):
        self.p = event.pos()
        a = self.sender()
        a.raise_()

    def mouseMoveEvent(self, event):
        self.setWindowTitle('Mouse')
