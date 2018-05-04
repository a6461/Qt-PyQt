from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        for color in QColor.colorNames():
            self.comboBox.addItem(color.upper())

    def on_comboBox_currentTextChanged(self, text):
        self.frame.setStyleSheet("background-color: %s" % text)
