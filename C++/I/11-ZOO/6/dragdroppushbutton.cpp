#include "dragdroppushbutton.h"
#include "form.h"

DragDropPushButton::DragDropPushButton(QWidget *parent):
    QPushButton(parent){}

void DragDropPushButton::dragEnterEvent(QDragEnterEvent *event)
{
    ((Form*)parent())->dragEnterEvent(event);
}
