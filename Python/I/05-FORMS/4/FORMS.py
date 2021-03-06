from form import *
from PyQt5.QtCore import *
import sys

def main():
    app = QApplication(sys.argv)
    translator = QTranslator(app)
    translator.load('qtbase_' + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)
    form = Form()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
