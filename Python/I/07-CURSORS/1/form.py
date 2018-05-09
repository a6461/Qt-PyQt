from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class Form(Ui_Form, QWidget):
    nam = []
    cur = []
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        #self.setCursor(QCursor(Qt.CursorShape(2)))
        mo = self.pushButton.staticMetaObject
        mp = mo.property(28)
        print(mp.read())
