#ifndef CURSORBUTTON_H
#define CURSORBUTTON_H

#include <QMouseEvent>
#include <QPushButton>

class CursorButton : public QPushButton
{
    Q_OBJECT

    int _tag;
public:
    CursorButton(QWidget *parent = 0);
    void setTag(int tag);
    int tag();
    void mousePressEvent(QMouseEvent *event);
};

#endif // CURSORBUTTON_H
