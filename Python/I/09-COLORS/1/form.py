from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.horizontalSlider_2.valueChanged.connect(
            self.on_horizontalSlider_valueChanged)
        self.horizontalSlider_3.valueChanged.connect(
            self.on_horizontalSlider_valueChanged)
        self.horizontalSlider_4.valueChanged.connect(
            self.on_horizontalSlider_valueChanged)    
        
    def on_horizontalSlider_valueChanged(self):
        self.label_6.setStyleSheet(
            'background-color: rgba({},{},{},{}); color: white'
                .format(self.horizontalSlider_2.value(),
                    self.horizontalSlider_3.value(),
                    self.horizontalSlider_4.value(),
                    self.horizontalSlider.value() / 255.0))
