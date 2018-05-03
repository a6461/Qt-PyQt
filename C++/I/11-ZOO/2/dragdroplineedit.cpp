#include "dragdroplineedit.h"
#include "dragdroplabel.h"

DragDropLineEdit::DragDropLineEdit(QWidget *parent):
    QLineEdit(parent){}

void DragDropLineEdit::dragEnterEvent(QDragEnterEvent *event)
{
    if (text() == "")
        event->accept();
    else
        event->ignore();
}

void DragDropLineEdit::dropEvent(QDropEvent *event)
{
    DragDropLabel *lb = (DragDropLabel*)event->source();
    setText(lb->text());
    lb->setVisible(false);
}
