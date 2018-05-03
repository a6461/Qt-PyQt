#include "dragdroplabel.h"
#include <QDrag>
#include <QMimeData>

DragDropLabel::DragDropLabel(QWidget *parent):
    QLabel(parent){}

void DragDropLabel::mousePressEvent(QMouseEvent *event)
{
    if (event->buttons() == Qt::LeftButton)
    {
        QPalette palette = this->palette();
        palette.setColor(QPalette::Foreground, Qt::blue);
        setPalette(palette);
        QDrag *drag = new QDrag(this);
        drag->setMimeData(new QMimeData());
        drag->exec(Qt::MoveAction);
        QRect rect = ((QWidget*)parent())->rect();
        QPoint pos = ((QWidget*)parent())->mapFromGlobal(QCursor::pos());
        if (!rect.contains(pos))
            setVisible(false);
        palette.setColor(QPalette::Foreground, Qt::black);
        setPalette(palette);
    }
}

void DragDropLabel::dragEnterEvent(QDragEnterEvent *event)
{
    event->accept();
    QPalette palette = this->palette();
    palette.setColor(QPalette::Background, Qt::yellow);
    setPalette(palette);
}

void DragDropLabel::dropEvent(QDropEvent *event)
{
    DragDropLabel *lb = (DragDropLabel*)event->source();
    QPalette palette = this->palette();
    palette.setColor(QPalette::Background, QColor("#F0F0f0"));
    setPalette(palette);
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

void DragDropLabel::dragLeaveEvent(QDragLeaveEvent*)
{
    QPalette palette = this->palette();
    palette.setColor(QPalette::Background, QColor("#F0F0f0"));
    setPalette(palette);
}
