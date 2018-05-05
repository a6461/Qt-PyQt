from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.label_6.setStyleSheet('background-color: black; color: white')
        self.horizontalSlider.valueChanged.connect(self.setColor)
        self.horizontalSlider_2.valueChanged.connect(self.setColor)
        self.horizontalSlider_3.valueChanged.connect(self.setColor)
        self.horizontalSlider_4.valueChanged.connect(self.setColor)
        self.horizontalSlider_5.valueChanged.connect(self.grayScale)
        self.setColor()
        
    def setColor(self):
        c = QColor(self.horizontalSlider_2.value(),
                self.horizontalSlider_3.value(),
                self.horizontalSlider_4.value(),
                self.horizontalSlider.value())
        self.label_6.setStyleSheet(
            'background-color: rgba({},{},{},{}); color: rgb({},{},{})'
                .format(c.red(), c.green(), c.blue(), c.alpha() / 255.0,
                        255 ^ c.red(), 255 ^ c.green(), 255 ^ c.blue()))
        self.label_6.setText('{:02X}{}'.format(c.alpha(), c.name().upper()[1:]))

    def grayScale(self):
        value = self.horizontalSlider_5.value()
        self.horizontalSlider_2.setValue(value)
        self.horizontalSlider_3.setValue(value)
        self.horizontalSlider_4.setValue(value)
