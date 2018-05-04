#ifndef DRAGDROPPUSHBUTTON_H
#define DRAGDROPPUSHBUTTON_H

#include <QDragEnterEvent>
#include <QPushButton>

class DragDropPushButton : public QPushButton
{
public:
    DragDropPushButton(QWidget *parent = 0);
    void dragEnterEvent(QDragEnterEvent *event);
};

#endif // DRAGDROPPUSHBUTTON_H
