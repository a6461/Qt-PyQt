#include "form3.h"
#include "ui_form3.h"

Form3::Form3(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Form3)
{
    ui->setupUi(this);
    setFixedSize(size());
}

Form3::~Form3()
{
    delete ui;
}
