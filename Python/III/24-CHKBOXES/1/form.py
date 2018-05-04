from ui_form import *
from form2 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.openSubWindow)
        self.form2 = Form2()
        self.form2.buttonBox.accepted.connect(self.changeLabels)

    def openSubWindow(self):
        self.form2.exec_()

    def changeLabels(self):
        for i in range(3):
            s = ''
            lw = self.form2.horizontalLayout.itemAt(i).widget()
            k = 0
            checkedItems = []
            for j in range(lw.count()):
                if lw.item(j).checkState() == Qt.Checked:
                    k += 1
                    checkedItems.append(lw.item(j).text())
            if k == 0:
                s = 'Пункты не выбраны'
            elif k == lw.count():
                s = 'Выбраны все пункты'
            else:
                for j in checkedItems:
                    s += ' ' + str(j)
                s = 'Bыбрано: ' + s
            self.formLayout.itemAt(2 * i + 1).widget().setText(s)
