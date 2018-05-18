from form import *
import sys
import ctypes

def main():
    appid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
