from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from form2 import *
from form3 import *

class Form(Ui_Form, QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.form2 = Form2()
        self.form3 = Form3()
        self.form2.setWindowFlags(
            Qt.Dialog | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.form3.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.pushButton.clicked.connect(self.showSubWindow)
        self.pushButton_2.clicked.connect(self.showDialog)

    def showSubWindow(self):
        self.form2.move(self.geometry().right() - 10,
                   self.geometry().bottom() - 10)
        self.form2.show()

    def showDialog(self):
        self.form3.show()
