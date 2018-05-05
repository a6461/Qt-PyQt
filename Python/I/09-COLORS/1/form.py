from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.label_6.setStyleSheet("background-color: black; color: white")
        self.horizontalSlider.valueChanged.connect(self.setColor)
        self.horizontalSlider_2.valueChanged.connect(self.setColor)
        self.horizontalSlider_3.valueChanged.connect(self.setColor)
        self.horizontalSlider_4.valueChanged.connect(self.setColor)
        
    def setColor(self):
        self.label_6.setStyleSheet("background-color: rgba({},{},{},{})"
            .format(self.horizontalSlider_2.value(),
                    self.horizontalSlider_3.value(),
                    self.horizontalSlider_4.value(),
                    self.horizontalSlider.value() / 255.0))
