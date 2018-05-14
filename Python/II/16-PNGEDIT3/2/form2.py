from ui_form2 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form2(Ui_Form2, QDialog):    
    def __init__(self, parent = None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.buttonBox.accepted.connect(self.new)

    def new(self):
        w = self.spinBox.value() - 4
        h = self.spinBox_2.value() - 4
        pix = QPixmap(w, h)
        pix.fill(Qt.white)
        self.parent().label.setPixmap(pix)
