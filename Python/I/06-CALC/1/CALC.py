from form import *
from PyQt5.QtCore import *
import sys

def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
