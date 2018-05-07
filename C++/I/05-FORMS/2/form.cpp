#include "form.h"
#include "ui_form.h"
#include <iostream>

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    setFixedSize(size());
    form2->setWindowFlags(Qt::Dialog | Qt::WindowMinMaxButtonsHint | Qt::WindowCloseButtonHint);
    form3->setWindowFlags(Qt::Dialog | Qt::WindowCloseButtonHint);
}

Form::~Form()
{
    delete ui;
}

void Form::on_pushButton_clicked()
{
    form2->move(geometry().right() - 10, geometry().bottom() - 10);
    form2->setVisible(!form2->isVisible());
    ui->pushButton->setText(form2->isVisible() ? "Закрыть подчиненное окно" :
        "Открыть подчиненное окно");
}

void Form::on_pushButton_2_clicked()
{
    form3->show();
}
