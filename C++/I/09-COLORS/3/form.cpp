#include "form.h"
#include "ui_form.h"

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);

    connect(ui->horizontalSlider_2, SIGNAL(valueChanged(int)), this, SLOT(on_horizontalSlider_valueChanged()));
    connect(ui->horizontalSlider_3, SIGNAL(valueChanged(int)), this, SLOT(on_horizontalSlider_valueChanged()));
    connect(ui->horizontalSlider_4, SIGNAL(valueChanged(int)), this, SLOT(on_horizontalSlider_valueChanged()));
    on_horizontalSlider_valueChanged();
}

Form::~Form()
{
    delete ui;
}

void Form::on_horizontalSlider_valueChanged()
{
    QColor c = QColor(ui->horizontalSlider_2->value(), ui->horizontalSlider_3->value(),
        ui->horizontalSlider_4->value(), ui->horizontalSlider->value());
    ui->label_6->setStyleSheet(QString("background-color: rgba(%1,%2,%3,%4); color: rgb(%5,%6,%7)")
        .arg(c.red()).arg(c.green()).arg(c.blue()).arg(c.alpha() / 255.0)
        .arg(255 ^ c.red()).arg(255 ^ c.green()).arg(255 ^ c.blue()));
    ui->label_6->setText(QString("%1%2").arg(QString::number(c.alpha(), 16).toUpper(), 2, '0')
        .arg(c.name().remove(0, 1).toUpper()));
}

void Form::on_horizontalSlider_5_valueChanged()
{
    int value = ui->horizontalSlider_5->value();
    ui->horizontalSlider_2->setValue(value);
    ui->horizontalSlider_3->setValue(value);
    ui->horizontalSlider_4->setValue(value);
}
