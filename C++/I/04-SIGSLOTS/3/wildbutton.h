#ifndef WILDBUTTON_H
#define WILDBUTTON_H

#include <QMouseEvent>
#include <QPushButton>

class WildButton : public QPushButton
{
    Q_OBJECT
public:
    WildButton(QWidget *parent = 0);
protected:
    void mouseMoveEvent(QMouseEvent *event);
signals:
    void mouseMoved();
};

#endif // WILDBUTTON_H
