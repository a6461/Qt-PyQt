from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from form2 import *
from imagelabel import *
import os

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.label = ImageLabel()
        self.label.setAlignment(Qt.AlignTop)
        self.label.setMouseTracking(True)
        self.scrollArea.setWidget(self.label)
        self.form2 = Form2(self)
        self.form2.spinBox.setValue(self.scrollArea.width())
        self.form2.spinBox_2.setValue(self.scrollArea.height())
        self.pushButton.clicked.connect(self.new)
        self.pushButton_2.clicked.connect(self.open)
        self.pushButton_3.clicked.connect(self.save)
        self.form2.new()
        self.label.mouseMoved.connect(self.mouseMove)

    def new(self):
        self.form2.spinBox.setFocus(True)
        if self.form2.exec_() == 1:
            self.setWindowTitle('Image Editor')

    def open(self):
        s = QFileDialog.getOpenFileName(self, 'Открытие', '',
            'Image files (*.bmp *.jpg *.png)')[0]
        if s:
            self.label.setPixmap(QPixmap(s, '1'))
            self.setWindowTitle('Image Editor - ' + s)

    def save(self):
        s = QFileDialog.getSaveFileName(self, 'Открытие', '',
            'PNG-files (*.png)')[0]
        if s:
            self.label.pixmap().save(s)
            self.setWindowTitle('Image Editor - ' + s)

    def mouseMove(self, event):
        self.label_2.setText('X,Y: {},{}'.format(event.x(), event.y()))
