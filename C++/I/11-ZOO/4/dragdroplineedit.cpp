#include "dragdroplineedit.h"
#include "dragdroplabel.h"

DragDropLineEdit::DragDropLineEdit(QWidget *parent):
    QLineEdit(parent){}

void DragDropLineEdit::dragEnterEvent(QDragEnterEvent *event)
{
    event->accept();
}

void DragDropLineEdit::dropEvent(QDropEvent *event)
{
    DragDropLabel *lb = (DragDropLabel*)event->source();
    if (lb->tag() >= tag())
    {
        setText(lb->text());
        setTag(lb->tag());
    }
    lb->setVisible(false);
}
