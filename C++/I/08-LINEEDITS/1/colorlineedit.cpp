#include "colorlineedit.h"
#include <QApplication>
#include <QKeyEvent>
#include <iostream>

ColorLineEdit::ColorLineEdit(QWidget *parent):
   QLineEdit(parent){}

void ColorLineEdit::focusInEvent(QFocusEvent *)
{
    setStyleSheet("background-color: darkGreen; color: white");
    selectAll();
    cursorForward(true);
    /*selectAll();
    QKeyEvent* event = new QKeyEvent(QEvent::KeyPress, Qt::Key_Right, Qt::NoModifier);
    QApplication::sendEvent(this, event);
    deselect();*/
}

void ColorLineEdit::focusOutEvent(QFocusEvent *)
{
    setStyleSheet("background-color: Window; color: WindowText");
    selectAll();
    deselect();
}
