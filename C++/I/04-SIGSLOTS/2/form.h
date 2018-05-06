#ifndef FORM_H
#define FORM_H

#include <QMouseEvent>
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

protected:
    void mousePressEvent(QMouseEvent *event);

private slots:
    void wildButtonMove();

    void on_pushButton_2_clicked();

private:
    Ui::Form *ui;
};

#endif // FORM_H
