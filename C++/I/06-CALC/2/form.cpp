#include "form.h"
#include "ui_form.h"
#include <QPushButton>

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    setFixedSize(size());
    connect(ui->pushButton_2, SIGNAL(clicked()), this, SLOT(on_pushButton_clicked()));
    connect(ui->pushButton_3, SIGNAL(clicked()), this, SLOT(on_pushButton_clicked()));
    connect(ui->pushButton_4, SIGNAL(clicked()), this, SLOT(on_pushButton_clicked()));
}

Form::~Form()
{
    delete ui;
}

void Form::on_pushButton_clicked()
{
    ui->label->setText(((QPushButton*) sender())->text());
}
