from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dragdropgroupbox import *
from dragdroplabel import *
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
        for i in range(len(self.groupBox_2.children())):
            self.groupBox_2.children()[i].deleteLater()
        for i in range(len(self.groupBox_3.children())):
            self.groupBox_3.children()[i].deleteLater()
        n = self.spinBox.value()
        w = self.groupBox.width()
        h = self.groupBox.height()
        for i in range(0, n):
            lb = DragDropLabel(self.groupBox)
            lb.setAutoFillBackground(True)
            lb.setFrameShape(QFrame.Box)
            lb.resize((w - 10) * (n - i) / n, (h - 15) / n)
            lb.move((w - lb.width()) / 2, h - 2 - (i + 1) * lb.height())
            lb.setStyleSheet("background-color: rgb({},{},{})".format(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            lb.show()
