from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

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

    def on_label_3_clicked(self):
        r = self.listWidget.currentRow()
        if r == -1:
            self.on_label_clicked()
        else:
            self.listWidget.insertItem(r, self.comboBox.currentText())
            self.listWidget.setCurrentRow(r)

    def on_label_4_clicked(self):
        r = self.listWidget.currentRow()
        if r <= 0:
            return
        else:
            x = self.listWidget.item(r).text()
            self.listWidget.item(r).setText(self.listWidget.item(r - 1).text())
            self.listWidget.item(r - 1).setText(x)
            self.listWidget.setCurrentRow(r - 1)

    def on_label_5_clicked(self):
        r = self.listWidget.currentRow()
        if r == self.listWidget.count() - 1:
            return
        else:
            x = self.listWidget.item(r).text()
            self.listWidget.item(r).setText(self.listWidget.item(r + 1).text())
            self.listWidget.item(r + 1).setText(x)
            self.listWidget.setCurrentRow(r + 1)

    def on_label_6_clicked(self):
        c = self.listWidget.count()
        if c == 0:
            return
        with open('LISTWDG1.dat', 'w') as f:
            for i in range(c):
                f.write(self.listWidget.item(i).text() + '\n')

    def on_label_7_clicked(self):
        if not os.path.exists('LISTWDG1.dat'):
            return
        self.listWidget.clear()
        with open('LISTWDG1.dat', 'r') as f:
            for line in f:
                self.listWidget.addItem(line[:-1])
        self.listWidget.setCurrentRow(self.listWidget.count() - 1)
