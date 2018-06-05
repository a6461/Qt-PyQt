from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.lineEdit.setFocus(True)
        self.radioButton_2.toggled[bool].connect(
            self.on_radioButton_toggled)
        
    def on_radioButton_toggled(self, checked):
        if not checked:
            return
        if self.sender() == self.radioButton:
            for i in range(4):
                for j in range(2):
                    self.setTabOrder(
                        self.gridLayout.itemAtPosition(i, j).widget(),
                        self.gridLayout.itemAtPosition(i, j + 1).widget())
            for i in range(3):
                self.setTabOrder(self.gridLayout.itemAtPosition(i, 2).widget(),
                    self.gridLayout.itemAtPosition(i + 1, 0).widget())
        else:
            for i in range(3):
                for j in range(3):
                    self.setTabOrder(
                        self.gridLayout.itemAtPosition(i, j).widget(),
                        self.gridLayout.itemAtPosition(i + 1, j).widget())
            for j in range(2):
                self.setTabOrder(self.gridLayout.itemAtPosition(3, j).widget(),
                    self.gridLayout.itemAtPosition(0, j + 1).widget())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F2:
            self.radioButton.setChecked(True)
        elif event.key() == Qt.Key_F3:
            self.radioButton_2.setChecked(True)
