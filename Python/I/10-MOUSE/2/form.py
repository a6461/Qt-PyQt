from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mouseframe import *

class Form(Ui_Form, QWidget):
    p = QPoint()
    s = QSize()
    
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
            #a.move(a.pos() + event.pos() - self.p)
            p0 = a.pos() + event.pos() - self.p
            a.move(max(0, p0.x()), max(0, p0.y()))
        elif event.buttons() == Qt.RightButton:
            #a.resize(self.s +
            #         QSize(event.x() - self.p.x(), event.y() - self.p.y()))
            s0 = self.s + QSize(event.x() - self.p.x(), event.y() - self.p.y())
            a.resize(max(50, s0.width()), max(20, s0.height()))
            
    def frameMousePress(self, event):
        self.p = event.pos()
        a = self.sender()
        a.raise_()
        self.s = a.size()

    def mouseMoveEvent(self, event):
        self.setWindowTitle('Mouse')
