#include "colorlineedit.h"
#include <QApplication>
#include <QKeyEvent>

ColorLineEdit::ColorLineEdit(QWidget *parent):
   QLineEdit(parent){}

void ColorLineEdit::focusInEvent(QFocusEvent *)
{
    setStyleSheet("background-color: darkGreen; color: white");
    selectAll();
    QApplication::sendEvent(this, new QKeyEvent(QEvent::KeyPress, Qt::Key_Right, Qt::NoModifier));
    deselect();
}

void ColorLineEdit::focusOutEvent(QFocusEvent *)
{
    selectAll();
    deselect();
    setStyleSheet("background-color: Window; color: WindowText");
    if (text() == "")
        setFocus();
}

