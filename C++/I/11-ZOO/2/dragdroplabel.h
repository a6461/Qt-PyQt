#ifndef DRAGDROPLABEL_H
#define DRAGDROPLABEL_H

#include <QMouseEvent>
#include <QLabel>

class DragDropLabel : public QLabel
{
public:
    DragDropLabel(QWidget *parent = 0);
    void mousePressEvent(QMouseEvent *event);
};

#endif // DRAGDROPLABEL_H
