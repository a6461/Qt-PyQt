#include "form.h"
#include "ui_form.h"

#include <QApplication>
#include <QDateTime>

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    connect(ui->pushButton_2, SIGNAL(mouseMoved()), this, SLOT(wildButtonMove()));
    qsrand(QDateTime::currentMSecsSinceEpoch());
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

void Form::wildButtonMove()
{
    if (QApplication::keyboardModifiers() == Qt::ControlModifier)
        return;
    ui->pushButton_2->move(qrand() % (rect().width() - 5),
                           qrand() % (rect().height() - 5));
}

void Form::on_pushButton_2_clicked()
{
    ui->pushButton_2->setText("Изменить");
    disconnect(ui->pushButton_2, SIGNAL(mouseMoved()), 0, 0);
}
