#include "form.h"
#include "ui_form.h"

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
}

Form::~Form()
{
    delete ui;
}

void Form::mousePressEvent(QMouseEvent *event)
{
    ui->pushButton->move(event->pos().x() - ui->pushButton->width() / 2,
        event->pos().y() - ui->pushButton->height() / 2);
}
