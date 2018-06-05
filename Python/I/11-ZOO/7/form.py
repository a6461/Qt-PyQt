from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.label.tag = 3
        self.label_2.tag = 2
        self.label_3.tag = 1
        self.label_4.tag = 0
        self.pushButton.setIcon(
            self.style().standardIcon(QStyle.SP_MessageBoxCritical))
        self.pushButton.clicked.connect(self.closeZoo)

    def dragEnterEvent(self, event):
        event.accept()
        
    def dropEvent(self, event):
        src = event.source()
        src.move(event.pos())

    def reload(self):
        for child in self.findChildren(QLabel):
            c = self.findChild(QLineEdit, 'lineEdit' + child.objectName()[5:])
            pos = self.horizontalLayoutWidget.mapToParent(c.pos())
            child.move(pos.x(), pos.y() / 2)
        self.pushButton.setFocus(True)

    def closeZoo(self):
        self.reload()
        for child in self.children()[0:4]:
            child.setVisible(True)
            c = self.findChild(QLineEdit, 'lineEdit' + child.objectName()[5:])
            c.setText('')
            c.tag = 0
        self.pushButton.setText('Зоопарк закрыт')
        self.pushButton.setStyleSheet('color: red;')
        self.pushButton.setIcon(
                self.style().standardIcon(QStyle.SP_MessageBoxCritical))
