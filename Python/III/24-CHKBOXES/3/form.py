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
        self.checkBox.stateChanged.connect(self.changeState)
        self.checkBox_2.stateChanged.connect(self.changeState)
        self.checkBox_3.stateChanged.connect(self.changeState)

    def openSubWindow(self):
        for i in range(3):
            lw = self.form2.horizontalLayout.itemAt(i).widget()
            if self.formLayout.itemAt(2 * i).widget().isChecked():
                for j in range(lw.count()):
                    lw.item(j).setCheckState(Qt.Checked)
        self.form2.exec_()

    def changeLabels(self):
        for i in range(3):
            lw = self.form2.horizontalLayout.itemAt(i).widget()
            cb = self.formLayout.itemAt(2 * i).widget()
            k = 0
            checkedItems = []
            for j in range(lw.count()):
                if lw.item(j).checkState() == Qt.Checked:
                    k += 1
                    checkedItems.append(lw.item(j).text())
            if k == 0:
                cb.setCheckState(Qt.Unchecked)
            elif k == lw.count():
                cb.setCheckState(Qt.Checked)
            else:
                s = ''
                for j in checkedItems:
                    s += ' ' + str(j)
                s = 'Bыбрано:' + s
                self.formLayout.itemAt(2 * i + 1).widget().setText(s)
                cb.setCheckState(Qt.PartiallyChecked)

    def changeState(self):
        cb = self.sender()
        if cb.checkState() == Qt.PartiallyChecked:
            return
        i = self.formLayout.indexOf(cb)
        self.formLayout.itemAt(i + 1).widget().setText(
            'Выбраны все пункты' if cb.checkState() == Qt.Checked
            else 'Пункты не выбраны')
