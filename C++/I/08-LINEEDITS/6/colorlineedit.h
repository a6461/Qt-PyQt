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
    void focusOutEvent(QFocusEvent *);
private slots:
    void on_textChanged();
};

#endif // COLORLINEEDIT_H
