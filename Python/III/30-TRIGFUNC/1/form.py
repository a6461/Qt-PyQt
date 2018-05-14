from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math

class Form(Ui_Form, QWidget):    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def toString(self, number):
        if number < 0.0000001:
            return '{:e}'.format(number)
        else:
            return '{:f}'.format(number)

    def showEvent(self, event):
        n = 7
        nMax = 1000001
        args = QCoreApplication.arguments()
        if len(args) > 1:
            try:
                n0 = int(args[1])
                if (n0 < 2) or (n0 > nMax):
                    raise Exception()
                else:
                    n = n
            except:
                s = 'Неверный параметр: {}\nДопустимые значения: от 2 до {}'.format(args[1], nMax)
                QMessageBox(QMessageBox.Critical, 'Ошибка', s).exec_()
                self.close()
                return

        step = 1 / (n - 1)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            x = i * step
            sx = math.sin(math.pi * x)
            cx = math.cos(math.pi * x)
            print(x, sx, cx)
            self.tableWidget.setItem(i, 0, QTableWidgetItem('{:f}'.format(x)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.toString(sx)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(self.toString(cx)))
            self.tableWidget.setItem(i, 3,
                QTableWidgetItem('{:e}'.format(sx / cx) if cx != 0 else 'бесконечность'))
            self.tableWidget.setItem(i, 4,
                QTableWidgetItem('{:e}'.format(cx / sx) if sx != 0 else 'бесконечность'))
                
                    
        
