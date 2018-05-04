#include "cursorbutton.h"
#include "form.h"

CursorButton::CursorButton(QWidget *parent):
   QPushButton(parent){}

void CursorButton::setTag(int tag)
{
    this->_tag = tag;
}

int CursorButton::tag()
{
    return _tag;
}

void CursorButton::mousePressEvent(QMouseEvent *event)
{
    Form *p = (Form*)parent()->parent();
    int c = p->names()->count();
    switch (event->button())
    {
        case Qt::LeftButton:
            _tag = (_tag + 1) % c;
            break;
        case Qt::RightButton:
            _tag = (_tag - 1 + c) % c;
            break;
        default:
            break;
    }
    setText(p->names()->at(_tag));
    setCursor(p->cursors()->at(_tag));
}
