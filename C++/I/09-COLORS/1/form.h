#ifndef FORM1_H
#define FORM1_H

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

private slots:
    void on_horizontalSlider_valueChanged();

private:
    Ui::Form *ui;
};

#endif // FORM1_H
