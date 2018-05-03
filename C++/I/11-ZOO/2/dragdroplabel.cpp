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
