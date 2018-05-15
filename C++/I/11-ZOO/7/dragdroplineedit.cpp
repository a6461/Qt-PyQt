#include "dragdroplineedit.h"
#include "dragdroplabel.h"

DragDropLineEdit::DragDropLineEdit(QWidget *parent):
    QLineEdit(parent){}

void DragDropLineEdit::dragEnterEvent(QDragEnterEvent *event)
{
    event->accept();
    setStyleSheet("background-color: yellow;");
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
    setStyleSheet(styleSheet().append("background-color: #f0f0f0;"));
}

void DragDropLineEdit::dragLeaveEvent(QDragLeaveEvent*)
{
    setStyleSheet("background-color: #f0f0f0;");
}
