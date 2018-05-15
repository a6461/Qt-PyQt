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
    DragDropLabel *src = (DragDropLabel*)event->source();
    if (src->tag() >= tag())
    {
        setText(src->text());
        setTag(src->tag());
    }
    src->setVisible(false);
}
