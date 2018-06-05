#ifndef FORM_H
#define FORM_H

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
    void on_radioButton_toggled(bool checked);

private:
    Ui::Form *ui;
    void keyPressEvent(QKeyEvent *event);
};

#endif // FORM_H
