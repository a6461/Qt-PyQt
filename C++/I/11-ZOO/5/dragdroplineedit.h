#ifndef DRAGDROPLINEEDIT_H
#define DRAGDROPLINEEDIT_H

#include <QDragEnterEvent>
#include <QDragLeaveEvent>
#include <QDropEvent>
#include <QLineEdit>

class DragDropLineEdit : public QLineEdit
{
    int _tag = 0;
public:
    DragDropLineEdit(QWidget *parent = 0);
    void dragEnterEvent(QDragEnterEvent *event);
    void dragLeaveEvent(QDragLeaveEvent *event);
    void dropEvent(QDropEvent *event);
    void setTag(const int& tag) { _tag = tag; }
    int tag() { return _tag; }
};

#endif // DRAGDROPLINEEDIT_H
