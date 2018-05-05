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
    equalSize = False
    font = QFont()
    
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
        self.pushButton_5.clicked.connect(self.setFont)
        self.form2.new()
        self.label.mouseMoved.connect(self.mouseMove)
        self.label.mousePressed.connect(self.mousePress)
        self.label.mouseReleased.connect(self.mouseRelease)
        self.label_3.backColorChanged.connect(self.changePenColor)
        self.label_5.backColorChanged.connect(self.changeBrushColor)
        self.label_6.mousePressed.connect(self.changeFigure)
        self.label_6.painted.connect(self.paintPattern)
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setJoinStyle(Qt.MiterJoin)
        self.radioButton.toggled.connect(self.changeMode)
        self.radioButton_2.toggled.connect(self.changeMode)
        self.radioButton_3.toggled.connect(self.changeMode)
        self.radioButton_4.toggled.connect(self.changeMode)
        self.pix = QPixmap(self.label.pixmap())
        self.lineEdit.cursorPositionChanged.connect(self.lineEditEnter)
        self.comboBox.currentIndexChanged.connect(self.changePenStyle)
        sz = QSize(self.comboBox.width() - 8, self.comboBox.height())
        self.comboBox.setIconSize(sz)
        for i in range(1, 6):
            bmp = QBitmap(sz)
            bmp.clear()
            painter = QPainter(bmp)
            painter.setPen(QPen(Qt.black, 2, i))
            painter.drawLine(0, sz.height() / 2, sz.width(), sz.height() / 2)
            painter.end()
            self.comboBox.addItem(QIcon(bmp), '')

    def new(self):
        self.form2.spinBox.setFocus(True)
        if self.form2.exec_() == 1:
            self.setWindowTitle('Image Editor')
            self.updateOldPixmap()

    def open(self):
        s = QFileDialog.getOpenFileName(self, 'Открытие', '',
            'Image files (*.bmp *.jpg *.png *.gif)')[0]
        if s:
            if os.path.splitext(s)[1] == '.gif':
                self.label.setMovie(QMovie(s))
                self.label.movie().start()
            else:
                self.label.setPixmap(QPixmap(s, '1'))
            self.setWindowTitle('Image Editor - ' + s)
            self.updateOldPixmap()

    def save(self):
        s = QFileDialog.getSaveFileName(self, 'Открытие', '',
            'PNG-files (*.png)')[0]
        if s:
            self.label.pixmap().save(s)
            self.setWindowTitle('Image Editor - ' + s)

    def clear(self):
        self.updateOldPixmap()
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
            elif self.mode < 3:
                modifiers = QApplication.keyboardModifiers()
                self.equalSize = modifiers == Qt.ControlModifier
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
            elif self.mode == 2:
                self.drawFigure(QRect(self.startPt, self.movePt), painter)
            else:
                painter.setBrush(self.brush)
                painter.setFont(self.font)
                painter.drawText(event.pos(), self.lineEdit.text())
            self.label.repaint()

    def mousePress(self, event):
        self.updateOldPixmap()
        self.movePt = self.startPt = event.pos()
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.AltModifier:
            c = QColor(self.label.pixmap().toImage().pixel(event.pos()))
            if event.buttons() == Qt.LeftButton:
                self.label_3.setStyleSheet('background-color: rgb({},{},{})'
                    .format(c.red(), c.green(), c.blue()))
                self.changePenColor()
            else:
                self.label_5.setStyleSheet('background-color: rgb({},{},{})'
                    .format(c.red(), c.green(), c.blue()))
                self.changeBrushColor()

    def changePenColor(self):
        self.pen.setColor(self.label_3.palette().color(QPalette.Background))
        self.label_6.repaint()

    def changeBrushColor(self):
        self.brush.setColor(self.label_5.palette().color(QPalette.Background))
        self.label_6.repaint()

    def on_spinBox_valueChanged(self, value):
        self.pen.setWidth(int(value))
        self.label_6.repaint()

    def changeMode(self):
        rb = self.sender()
        if not rb.isChecked():
            return
        self.mode = self.verticalLayout_2.indexOf(rb)

    def reversibleDraw(self):
        painter = QPainter(self.label.pixmap())
        painter.setCompositionMode(QPainter.RasterOp_NotSourceXorDestination)
        if self.mode == 1:
            painter.drawLine(self.startPt, self.movePt)
        else:
            painter.setPen(QPen(Qt.black, 1, self.figureMode + 1))
            painter.drawRect(self.newRect(QRect(self.startPt, self.movePt)))
        self.label.repaint()

    def newRect(self, rect):
        if self.equalSize:
            if rect.width() > rect.height():
                rect.setRight(rect.x() + rect.height())
            else:
                rect.setBottom(rect.y() + rect.width())
        w = self.pen.width()
        return QRect(rect.x() + w / 2, rect.y() + w / 2,
                  rect.width() - w + 1, rect.height() - w + 1)

    def drawFigure(self, rect, painter, pattern=True):
        painter.setPen(self.pen)
        if not self.checkBox.isChecked():
            painter.setBrush(self.brush)
        if pattern:
            r = self.newRect(rect)
        else:
            r = rect
        if self.figureMode == 0:
            painter.drawRect(r)
        elif self.figureMode == 1:
            painter.drawEllipse(r)

    def paintPattern(self):
        painter = QPainter()
        painter.begin(self.label_6)
        r = self.label_6.rect()
        self.drawFigure(QRect(0, 0, self.label_6.width() - 1, self.label_6.height() - 1),
                        painter, False)
        painter.end()

    def changeFigure(self):
        self.radioButton_3.setChecked(True)
        self.figureMode = (self.figureMode + 1) % 2
        self.label_6.repaint()

    def on_checkBox_stateChanged(self):
        self.label_6.repaint()

    def updateOldPixmap(self):
        self.pix = QPixmap(self.label.pixmap())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.label.setPixmap(self.pix)

    def lineEditEnter(self):
        self.radioButton_4.setChecked(True)

    def setFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font = font
            self.lineEdit.setFont(font)

    def changePenStyle(self):
        self.pen.setStyle(self.comboBox.currentIndex() + 1)
        self.label_6.repaint()
