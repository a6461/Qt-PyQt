#include "colorlineedit.h"
#include <QApplication>
#include <QKeyEvent>
#include <iostream>

ColorLineEdit::ColorLineEdit(QWidget *parent):
   QLineEdit(parent){}

void ColorLineEdit::focusInEvent(QFocusEvent *)
{
    setStyleSheet("background-color: darkGreen; color: white");
}

void ColorLineEdit::focusOutEvent(QFocusEvent *)
{
    setStyleSheet("background-color: Window; color: WindowText");
}
