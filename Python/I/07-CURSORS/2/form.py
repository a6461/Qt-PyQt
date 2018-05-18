from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):
    names = []
    cursors = []

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.names = self.enumToStr(Qt, Qt.CursorShape)
        self.cursors = [QCursor(Qt.CursorShape(i))
                        for i in range(len(self.names))]
        self.pushButton.setProperty(
            'tag', self.names.index('ArrowCursor'))

    def enumToStr(self, namespace, enum):
        names = {}
        for value in dir(namespace):
            key = getattr(namespace, value)
            if isinstance(key, enum):
                names[key] = value
        names = [value for (key, value) in sorted(names.items())]
        return names
           
    def on_pushButton_mousePressed(self, event):
        k = self.pushButton.property('tag')
        c = len(self.names)
        if event.buttons() == Qt.LeftButton:
            k = (k + 1) % c
        elif event.buttons() == Qt.RightButton:
            k = (k - 1 + c) % c
        self.pushButton.setText(self.names[k])
        self.pushButton.setCursor(self.cursors[k])
        self.pushButton.setProperty('tag', k)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.setCursor(self.pushButton.cursor())

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.setCursor(Qt.WaitCursor)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        self.setCursor(Qt.ArrowCursor)
