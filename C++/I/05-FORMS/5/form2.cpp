#include "form2.h"
#include "ui_form2.h"

Form2::Form2(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Form2)
{
    ui->setupUi(this);
}

Form2::~Form2()
{
    delete ui;
}

void Form2::showEvent(QShowEvent *)
{
    ui->label->setText(QString("Окно открыто в %1-й раз.").arg(++count));
    emit visibleChanged(false);
}

void Form2::closeEvent(QCloseEvent*)
{
    emit visibleChanged(true);
}

