#ifndef ICONBUTTON_H
#define ICONBUTTON_H

#include <QPushButton>

class IconButton : public QPushButton
{
    Q_OBJECT

    int _tag;
public:
    IconButton(QWidget *parent = 0);
    void setTag(int tag) { _tag = tag; }
    int tag() { return _tag; }
};

#endif // ICONBUTTON_H
