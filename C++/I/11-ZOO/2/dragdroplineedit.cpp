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
    DragDropLabel *src = (DragDropLabel*)event->source();
    setText(src->text());
    src->setVisible(false);
}
