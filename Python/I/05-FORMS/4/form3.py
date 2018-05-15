from ui_form3 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form3(Ui_Form3, QDialog):
    windowTitlesChanged = pyqtSignal(str, str)
    
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())

    def on_buttonBox_clicked(self, button):
        if button != self.buttonBox.button(QDialogButtonBox.Cancel):
            self.windowTitlesChanged.emit(
                self.lineEdit.text(), self.lineEdit_2.text())
