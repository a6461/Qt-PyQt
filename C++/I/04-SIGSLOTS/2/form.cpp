#include "form.h"
#include "ui_form.h"

#include <QApplication>
#include <QDateTime>

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    connect(ui->button_2, SIGNAL(mouseMoved()), this, SLOT(wildButtonMove()));
    qsrand(QDateTime::currentMSecsSinceEpoch());
}

Form::~Form()
{
    delete ui;
}

void Form::mousePressEvent(QMouseEvent *event)
{
    ui->button->move(event->x() - ui->button->width() / 2,
        event->y() - ui->button->height() / 2);
}

void Form::wildButtonMove()
{
    if (QApplication::keyboardModifiers() == Qt::ControlModifier)
        return;
    ui->button_2->move(qrand() % (width() - 5), qrand() % (height() - 5));
}

void Form::on_button_2_clicked()
{
    ui->button_2->setText("Изменить");
    disconnect(ui->button_2, SIGNAL(mouseMoved()), 0, 0);
}
