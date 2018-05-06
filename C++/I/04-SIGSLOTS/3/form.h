#ifndef FORM_H
#define FORM_H

#include <QMouseEvent>
#include <QResizeEvent>
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
    void resizeEvent(QResizeEvent *event);

private slots:
    void wildButtonMove();
    void on_pushButton_2_clicked();
    void changeWindowState();

private:
    Ui::Form *ui;
};

#endif // FORM_H
