#-------------------------------------------------
#
# Project created by QtCreator 2016-05-27T22:57:46
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = CURSORS
TEMPLATE = app


SOURCES += main.cpp\
        form.cpp \
    cursorbutton.cpp \
    iconbutton.cpp

HEADERS  += form.h \
    cursorbutton.h \
    iconbutton.h

FORMS    += \
    form.ui

RESOURCES += \
    cursors.qrc
