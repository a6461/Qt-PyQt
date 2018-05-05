#include "form.h"
#include "ui_form.h"

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    setFixedSize(size());

    ui->label_6->setStyleSheet("background-color: black; color: white");
    connect(ui->horizontalSlider_2, SIGNAL(valueChanged(int)), this, SLOT(on_horizontalSlider_valueChanged()));
    connect(ui->horizontalSlider_3, SIGNAL(valueChanged(int)), this, SLOT(on_horizontalSlider_valueChanged()));
    connect(ui->horizontalSlider_4, SIGNAL(valueChanged(int)), this, SLOT(on_horizontalSlider_valueChanged()));
}

Form::~Form()
{
    delete ui;
}

void Form::on_horizontalSlider_valueChanged()
{
    ui->label_6->setStyleSheet(QString("background-color: rgba(%1,%2,%3,%4)")
        .arg(ui->horizontalSlider_2->value()).arg(ui->horizontalSlider_3->value())
        .arg(ui->horizontalSlider_4->value()).arg(ui->horizontalSlider->value() / 255.0));
}
