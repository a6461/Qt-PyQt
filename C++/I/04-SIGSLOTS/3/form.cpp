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
    ui->button->move(event->pos().x() - ui->button->width() / 2,
        event->pos().y() - ui->button->height() / 2);
    if (ui->button_2->text() != "")
    {
        ui->button_2->setText("");
        connect(ui->button_2, SIGNAL(mouseMoved()), this, SLOT(wildButtonMove()));
        connect(ui->button_2, SIGNAL(clicked()), this, SLOT(on_button_2_clicked()));
        disconnect(ui->button_2, SIGNAL(clicked()), this, SLOT(changeWindowState()));
    }
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
    disconnect(ui->button_2, SIGNAL(clicked()), this, SLOT(on_button_2_clicked()));
    connect(ui->button_2, SIGNAL(clicked()), this, SLOT(changeWindowState()));
}

void Form::changeWindowState()
{
    if (windowState() == Qt::WindowNoState)
        setWindowState(Qt::WindowMaximized);
    else
        setWindowState(Qt::WindowNoState);
}

void Form::resizeEvent(QResizeEvent*)
{
    if (!rect().intersects(ui->button->geometry()))
        ui->button->move(10, 10);
    if (!rect().intersects(ui->button_2->geometry()))
        ui->button_2->move(10, 40);
}
