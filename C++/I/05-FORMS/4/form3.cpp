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

void Form3::on_buttonBox_clicked(QAbstractButton *button)
{
    if ((QPushButton*)button != ui->buttonBox->button(QDialogButtonBox::Cancel))
        emit windowTitlesChanged(ui->lineEdit->text(), ui->lineEdit_2->text());
}
