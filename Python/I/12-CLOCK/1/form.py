from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class Form(QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        uic.loadUi('form.ui', self)
        self.setFixedSize(self.size())
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.setTime)
        self.setTime()
        
    def setTime(self):
        self.label.setText(QDateTime.currentDateTime().toString('hh:mm:ss'))
