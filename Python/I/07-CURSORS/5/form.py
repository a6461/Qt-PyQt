from ui_form import *
from cursorbutton import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import resources

class Form(Ui_Form, QWidget):
    names = []
    cursors = []
    icons = []

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.names = self.enumToStr(Qt, Qt.CursorShape)
        self.cursors = [QCursor(Qt.CursorShape(i))
                        for i in range(len(self.names))]
        self.pushButton.setProperty(
            'tag', self.names.index('ArrowCursor'))
        for i in range (1, 3):
            self.names.append('C{}'.format(i))
            self.cursors.append(QCursor(QPixmap(':/C{}.cur'.format(i))))
        self.pushButton_5.setProperty('tag', 0)
        self.icons.append(
            self.style().standardIcon(QStyle.SP_TitleBarMenuButton))
        self.icons.append(
            self.style().standardIcon(QStyle.SP_ComputerIcon))
        self.icons.append(
            self.style().standardIcon(QStyle.SP_DirIcon))
        self.setWindowIcon(self.icons[0])
        self.trayIcon = QSystemTrayIcon()
        self.trayIcon.setIcon(self.icons[0])
        self.trayIcon.setToolTip('Icon in Traybar')
        self.trayIcon.setVisible(False)

    def enumToStr(self, namespace, enum):
        names = {}
        for value in dir(namespace):
            key = getattr(namespace, value)
            if isinstance(key, enum):
                names[key] = value
        names = [value for (key, value) in sorted(names.items())]
        return names

    def on_pushButton_mousePressed(self, event):
        k = self.pushButton.property('tag')
        c = len(self.names)
        if event.buttons() == Qt.LeftButton:
            k = (k + 1) % c
        elif event.buttons() == Qt.RightButton:
            k = (k - 1 + c) % c
        self.pushButton.setText(self.names[k])
        self.pushButton.setCursor(self.cursors[k])
        self.pushButton.setProperty('tag', k)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.setCursor(self.pushButton.cursor())

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.setCursor(Qt.WaitCursor)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        self.setCursor(Qt.ArrowCursor)

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        k = (self.pushButton_5.property('tag') + 1) % 3
        self.pushButton_5.setText('Icon {}'.format(k))
        self.pushButton_5.setProperty('tag', k)
        self.setWindowIcon(self.icons[k])

    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        b = self.pushButton_6.text() == 'Show Tray Icon'
        self.trayIcon.setVisible(b)
        if b:
            self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        else:
            self.setWindowFlag(Qt.Window)
        self.pushButton_6.setText('Hide Tray Icon' if b else 'Show Tray Icon')
