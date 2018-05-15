from ui_form2 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form2(Ui_Form2, QDialog):
    visibleChanged = pyqtSignal(bool)
    count = 0
    
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

    def showEvent(self, event):
        self.count += 1
        self.label.setText('Окно открыто в {}-й раз.'.format(self.count))
        self.visibleChanged.emit(False)

    def closeEvent(self, event):
        self.visibleChanged.emit(True)
