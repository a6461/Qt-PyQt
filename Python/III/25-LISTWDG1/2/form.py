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
        self.frame_2.setVisible(False)

    def on_comboBox_currentTextChanged(self, text):
        self.frame.setStyleSheet("background-color: %s" % text)

    def on_listWidget_currentRowChanged(self, row):
        self.frame_2.setVisible(row != -1)
        if row == -1:
            return
        self.frame_2.setStyleSheet("background-color: %s"
                                   % self.listWidget.currentItem().text())

    def on_label_clicked(self):
        self.listWidget.addItem(self.comboBox.currentText())
        self.listWidget.item(self.listWidget.count() - 1).setSelected(True)
        self.listWidget.setCurrentRow(self.listWidget.count() - 1)
        
    def on_label_2_clicked(self):
        self.listWidget.takeItem(self.listWidget.currentRow())
