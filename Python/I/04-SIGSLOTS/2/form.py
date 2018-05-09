from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.button_2.mouseMoved.connect(self.wildButtonMove)
        self.button_2.clicked.connect(self.wildButtonClick)

    def mousePressEvent(self, event):
        self.button.move(event.x() - self.button.width() / 2,
                     event.y() - self.button.height() / 2)

    def wildButtonMove(self):
        if QApplication.keyboardModifiers() == Qt.ControlModifier:
            return
        self.button_2.move(random.randrange(self.width() - 5),
                           random.randrange(self.height() - 5))

    def wildButtonClick(self):
        if not self.button_2.text():
            self.button_2.setText('Изменить')
            self.button_2.mouseMoved.disconnect()
