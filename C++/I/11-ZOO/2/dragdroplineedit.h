#ifndef DRAGDROPLINEEDIT_H
#define DRAGDROPLINEEDIT_H

#include <QDragEnterEvent>
#include <QDropEvent>
#include <QLineEdit>

class DragDropLineEdit : public QLineEdit
{
public:
    DragDropLineEdit(QWidget *parent = 0);
    void dragEnterEvent(QDragEnterEvent *event);
    void dropEvent(QDropEvent *event);
};

#endif // DRAGDROPLINEEDIT_H
