from ui_form import *
from PyQt5.QtWidgets import *
import random, sys

class Form(Ui_Form, QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.load()
        self.spinBox.valueChanged.connect(self.load)
        
    def load(self):
        for i in range(len(self.groupBox.children())):
            self.groupBox.children()[i].deleteLater()
        self.groupBox.findChildren(QLabel).clear()
        n = self.spinBox.value()
        w = self.groupBox.width()
        h = self.groupBox.height()
        for i in range(0, n):
            lb = QLabel(self.groupBox)
            lb.setAutoFillBackground(True)
            lb.setFrameShape(QFrame.Box)
            lb.resize((w - 10) * (n - i) / n, (h - 15) / n)
            lb.move((w - lb.width()) / 2, h - 2 - (i + 1) * lb.height())
            lb.setStyleSheet("background-color: RGB({}, {}, {})"
                             .format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            lb.show()
