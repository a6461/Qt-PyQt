from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def mousePressEvent(self, event):
        self.button.move(event.x() - self.button.width() / 2,
                     event.y() - self.button.height() / 2);
