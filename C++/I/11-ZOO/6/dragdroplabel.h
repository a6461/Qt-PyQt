#ifndef DRAGDROPLABEL_H
#define DRAGDROPLABEL_H

#include <QDragEnterEvent>
#include <QDragLeaveEvent>
#include <QDropEvent>
#include <QMouseEvent>
#include <QLabel>

class DragDropLabel : public QLabel
{
    Q_OBJECT

    int _tag;
public:
    DragDropLabel(QWidget *parent = 0);
    void mousePressEvent(QMouseEvent *event);
    void dragEnterEvent(QDragEnterEvent *event);
    void dragLeaveEvent(QDragLeaveEvent *event);
    void dropEvent(QDropEvent *event);
    void setTag(const int& tag) { _tag = tag; }
    int tag() { return _tag; }
signals:
    void buttonChanged();
};

#endif // DRAGDROPLABEL_H
