#include "wildbutton.h"

WildButton::WildButton(QWidget *parent):
    QPushButton(parent){}

void WildButton::mouseMoveEvent(QMouseEvent*)
{
    emit mouseMoved();
}
