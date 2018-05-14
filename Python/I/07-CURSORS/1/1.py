from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

pagesizes = {}
for key, value in vars(QFrame.Shadow).iteritems():
    if isinstance(value, QPrinter.PageSize):
        pagesizes[key] = value
        pagesizes[value] = key
