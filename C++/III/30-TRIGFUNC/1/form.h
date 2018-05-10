#ifndef FORM_H
#define FORM_H

#include <QShowEvent>
#include <QWidget>

namespace Ui {
class Form;
}

class Form : public QWidget
{
    Q_OBJECT

public:
    explicit Form(QWidget *parent = 0);
    ~Form();

private:
    Ui::Form *ui;
    void showEvent(QShowEvent*);
};

#endif // FORM_H
