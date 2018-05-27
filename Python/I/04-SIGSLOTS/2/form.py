from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def mousePressEvent(self, event):
        self.pushButton.move(event.x() - self.pushButton.width() / 2,
                             event.y() - self.pushButton.height() / 2)

    def on_pushButton_2_mouseMoved(self):
        if QApplication.keyboardModifiers() == Qt.ControlModifier:
            return
        self.pushButton_2.move(random.randrange(self.width() - 5),
                           random.randrange(self.height() - 5))

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        if not self.pushButton_2.text():
            self.pushButton_2.setText('Изменить')
            self.pushButton_2.mouseMoved.disconnect()
