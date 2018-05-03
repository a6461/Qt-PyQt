#include "dragdroplabel.h"
#include <QDrag>
#include <QMimeData>

DragDropLabel::DragDropLabel(QWidget *parent):
    QLabel(parent){}

void DragDropLabel::mousePressEvent(QMouseEvent *event)
{
    if (event->buttons() == Qt::LeftButton)
    {
        QDrag *drag = new QDrag(this);
        drag->setMimeData(new QMimeData());
        drag->exec(Qt::MoveAction);
    }
}

void DragDropLabel::dragEnterEvent(QDragEnterEvent *event)
{
    event->accept();
}

void DragDropLabel::dropEvent(QDropEvent *event)
{
    DragDropLabel *lb = (DragDropLabel*)event->source();
    if (this == lb)
        return;
    if (lb->tag() > tag())
    {
        lb->move(pos());
        setVisible(false);
    }
    else
        lb->setVisible(false);
}
