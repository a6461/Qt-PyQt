#include "form3.h"
#include "ui_form3.h"
#include "form.h"

Form3::Form3(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Form3)
{
    ui->setupUi(this);
}

Form3::~Form3()
{
    delete ui;
}

QString Form3::mainWindowText()
{
    return ui->lineEdit->text();
}

QString Form3::subWindowText()
{
    return ui->lineEdit_2->text();
}

void Form3::on_buttonBox_clicked(QAbstractButton *button)
{
    if ((QPushButton*)button == ui->buttonBox->button(QDialogButtonBox::Apply))
        ((Form*)parent())->setWindowTitles();
}
