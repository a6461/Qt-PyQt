from ui_form2 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form2(Ui_Form2, QDialog):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
