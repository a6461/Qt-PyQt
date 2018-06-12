from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mouseframe import *

class Form(Ui_Form, QScrollArea):
    p = QPoint()
    s = QSize()
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        #self.setWidget
        #self.frame_2.mouseMoved[QMouseEvent].connect(self.on_frame_mouseMoved)
        #self.frame_2.mousePressed[QMouseEvent].connect(self.on_frame_mousePressed)

    def on_frame_mouseMoved(self, event):
        a = self.sender()
        self.setWindowTitle('Mouse - {} {{X={},Y={}}}'.format(
            a.objectName(), event.x(), event.y()))
        if event.buttons() == Qt.LeftButton:
            #a.move(a.pos() + event.pos() - self.p)
            p0 = a.pos() + event.pos() - self.p
            a.move(max(0, p0.x()), max(0, p0.y()))
        elif event.buttons() == Qt.RightButton:
            #a.resize(self.s +
            #         QSize(event.x() - self.p.x(), event.y() - self.p.y()))
            s0 = self.s + QSize(event.x() - self.p.x(), event.y() - self.p.y())
            a.resize(max(50, s0.width()), max(20, s0.height()))
            
    def on_frame_mousePressed(self, event):
        self.p = event.pos()
        a = self.sender()
        a.raise_()
        self.s = a.size()

    def mouseMoveEvent(self, event):
        self.setWindowTitle('Mouse')
