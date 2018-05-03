#include "dragdroplineedit.h"
#include "dragdroplabel.h"

DragDropLineEdit::DragDropLineEdit(QWidget *parent):
    QLineEdit(parent){}

void DragDropLineEdit::dragEnterEvent(QDragEnterEvent *event)
{
    event->accept();
    QPalette palette = this->palette();
    palette.setColor(QPalette::Base, Qt::yellow);
    setPalette(palette);
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
    QPalette palette = this->palette();
    palette.setColor(QPalette::Base, QColor("#F0F0f0"));
    setPalette(palette);
}

void DragDropLineEdit::dragLeaveEvent(QDragLeaveEvent*)
{
    QPalette palette = this->palette();
    palette.setColor(QPalette::Base, QColor("#F0F0f0"));
    setPalette(palette);
}
