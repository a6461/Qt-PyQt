from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ColorLabel(QLabel):
    backColorChanged = pyqtSignal()
    
    def mousePressEvent(self, event):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet('background-color: rgb({},{},{})'
                    .format(color.red(), color.green(), color.blue()))
        self.backColorChanged.emit()
