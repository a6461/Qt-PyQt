from ui_form import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from form2 import *
from colorlabel import *
from imagelabel import *
import os, sys

class Form(Ui_Form, QWidget):
    startPt = QPoint()
    pen = QPen(Qt.black)
    mode = 0
    movePt = QPoint()
    nullPt = QPoint(sys.maxsize, 0)
    brush = QBrush(Qt.white)
    figureMode = 0
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.label = ImageLabel()
        self.label.setAlignment(Qt.AlignTop)
        self.label.setMouseTracking(True)
        self.scrollArea.setWidget(self.label)
        self.form2 = Form2(self)
        self.form2.spinBox.setValue(self.scrollArea.width())
        self.form2.spinBox_2.setValue(self.scrollArea.height())
        self.pushButton.clicked.connect(self.new)
        self.pushButton_2.clicked.connect(self.open)
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton_4.clicked.connect(self.clear)
        self.form2.new()
        self.label.mouseMoved.connect(self.mouseMove)
        self.label.mousePressed.connect(self.mousePress)
        self.label.mouseReleased.connect(self.mouseRelease)
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setJoinStyle(Qt.MiterJoin)
        self.radioButton.toggled.connect(self.setMode)
        self.radioButton_2.toggled.connect(self.setMode)
        self.radioButton_3.toggled.connect(self.setMode)
        self.pix = QPixmap(self.label.pixmap())

    def new(self):
        self.form2.spinBox.setFocus(True)
        if self.form2.exec_() == 1:
            self.setWindowTitle('Image Editor')

    def open(self):
        s = QFileDialog.getOpenFileName(self, 'Открытие', '',
            'Image files (*.bmp *.jpg *.png *.gif)')[0]
        if s:
            self.label.setPixmap(QPixmap(s, '1'))
            self.setWindowTitle('Image Editor - ' + s)

    def save(self):
        s = QFileDialog.getSaveFileName(self, 'Открытие', '',
            'PNG-files (*.png)')[0]
        if s:
            self.label.pixmap().save(s)
            self.setWindowTitle('Image Editor - ' + s)

    def clear(self):
        pix = self.label.pixmap()
        pix.fill(self.brush.color())
        self.label.setPixmap(pix)

    def mouseMove(self, event):
        self.label_2.setText('X,Y: {},{}'.format(event.x(), event.y()))
        if self.startPt == self.nullPt:
            return
        if event.buttons() == Qt.LeftButton:
            if self.mode == 0:
                painter = QPainter(self.label.pixmap())
                painter.setPen(self.pen)
                painter.drawLine(self.startPt, event.pos())
                self.startPt = event.pos()
                self.label.repaint()
            else:
                self.label.setPixmap(self.pix)
                self.movePt = event.pos()
                self.reversibleDraw()

    def mouseRelease(self, event):
        if self.startPt == self.nullPt:
            return
        if self.mode >= 1:
            self.label.setPixmap(self.pix)
            painter = QPainter(self.label.pixmap())
            painter.setPen(self.pen)
            if self.mode == 1:
                painter.drawLine(self.startPt, self.movePt)
            else:
                self.drawFigure(QRect(self.startPt, self.movePt), painter)
            self.label.repaint()

    def mousePress(self, event):
        self.pix = QPixmap(self.label.pixmap())
        self.movePt = self.startPt = event.pos()

    def on_label_3_backColorChanged(self):
        self.pen.setColor(self.label_3.palette().color(QPalette.Background))
        self.label_6.repaint()

    def on_label_5_backColorChanged(self):
        self.brush.setColor(self.label_5.palette().color(QPalette.Background))
        self.label_6.repaint()

    def on_spinBox_valueChanged(self, value):
        self.pen.setWidth(int(value))
        self.label_6.repaint()

    def setMode(self):
        rb = self.sender()
        if not rb.isChecked():
            return
        self.mode = self.verticalLayout_2.indexOf(rb)

    def drawFigure(self, rect, painter):
        w = self.pen.width()
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        r = QRect(rect.x() + w / 2, rect.y() + w / 2,
                  rect.width() - w + 1, rect.height() - w + 1)
        if self.figureMode == 0:
            painter.drawRect(r)
        elif self.figureMode == 1:
            painter.drawEllipse(r)

    def reversibleDraw(self):
        painter = QPainter(self.label.pixmap())
        painter.setCompositionMode(QPainter.RasterOp_NotSourceXorDestination)
        if self.mode == 1:
            painter.drawLine(self.startPt, self.movePt)
        else:
            painter.setPen(
                QPen(Qt.black, 2 - self.figureMode, self.figureMode + 1))
            painter.drawRect(QRect(self.startPt, self.movePt))
        self.label.repaint()

    def on_label_6_painted(self):
        painter = QPainter()
        painter.begin(self.label_6)
        r = self.label_6.rect()
        self.drawFigure(QRect(r.x(), r.y(), r.width() - 1, r.height() - 1),
                        painter)
        painter.end()

    def on_label_6_mousePressed(self):
        self.radioButton_3.setChecked(True)
        self.figureMode = (self.figureMode + 1) % 2
        self.label_6.repaint()
