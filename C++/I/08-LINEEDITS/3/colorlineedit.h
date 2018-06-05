#ifndef COLORLINEEDIT_H
#define COLORLINEEDIT_H

#include <QLineEdit>

class ColorLineEdit : public QLineEdit
{
    Q_OBJECT
public:
    ColorLineEdit(QWidget *parent = 0);
private:
    void focusInEvent(QFocusEvent *);
    void focusOutEvent(QFocusEvent *event);
};

#endif // COLORLINEEDIT_H
