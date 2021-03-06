#include "dragdroplabel.h"
#include <QDrag>
#include <QMimeData>

DragDropLabel::DragDropLabel(QWidget *parent):
    QLabel(parent){}

void DragDropLabel::mousePressEvent(QMouseEvent *event)
{
    if (event->buttons() == Qt::LeftButton)
    {
        setStyleSheet("color: blue;");
        QDrag *drag = new QDrag(this);
        drag->setMimeData(new QMimeData());
        drag->exec(Qt::MoveAction);
        QRect rect = ((QWidget*)parent())->rect();
        QPoint pos = ((QWidget*)parent())->mapFromGlobal(QCursor::pos());
        if (!rect.contains(pos))
            setVisible(false);
        setStyleSheet("color: black;");
        QString s = "";
        for (auto child = parent()->children().begin();
             child < parent()->children().begin() + 4; child++)
        {
            if (((DragDropLabel*)(*child))->isVisible())
                return;
            s += ((DragDropLabel*)(*child))->text();
        }
        if (s == "")
            return;
        emit buttonChanged();
    }
}

void DragDropLabel::dragEnterEvent(QDragEnterEvent *event)
{
    event->accept();
    setStyleSheet(styleSheet().append("background-color: yellow;"));
}

void DragDropLabel::dropEvent(QDropEvent *event)
{
    DragDropLabel *src = (DragDropLabel*)event->source();
    setStyleSheet(styleSheet().append("background-color: #f0f0f0;"));
    if (this == src)
        return;
    if (src->tag() > tag())
    {
        src->move(pos());
        setVisible(false);
    }
    else
        src->setVisible(false);
}

void DragDropLabel::dragLeaveEvent(QDragLeaveEvent*)
{
    setStyleSheet(styleSheet().append("background-color: #f0f0f0;"));
}
