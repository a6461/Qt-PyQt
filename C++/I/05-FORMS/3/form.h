#ifndef FORM_H
#define FORM_H

#include <QWidget>
#include "form2.h"
#include "form3.h"

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
    void on_pushButton_clicked();
    void on_pushButton_2_clicked();
    void setPushButtonText(bool visible);

private:
    Ui::Form *ui;
    Form2 *form2 = new Form2(this);
    Form3 *form3 = new Form3(this);
};

#endif // FORM_H
