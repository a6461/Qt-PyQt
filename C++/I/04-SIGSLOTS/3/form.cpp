#include "form.h"
#include "ui_form.h"

#include <QApplication>
#include <QDateTime>

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
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
    if (ui->pushButton_2->text() != "")
    {
        ui->pushButton_2->setText("");
        connect(ui->pushButton_2, SIGNAL(mouseMoved()), this, SLOT(on_pushButton_2_mouseMoved()));
        disconnect(ui->pushButton_2, SIGNAL(clicked()), 0, 0);
        connect(ui->pushButton_2, SIGNAL(clicked()), this, SLOT(on_pushButton_2_clicked()));
    }
}

void Form::on_pushButton_2_mouseMoved()
{
    std::cout << "moved" << std::endl;
    if (QApplication::keyboardModifiers() == Qt::ControlModifier)
        return;
    ui->pushButton_2->move(qrand() % (width() - 5), qrand() % (height() - 5));
}

void Form::on_pushButton_2_clicked()
{
    std::cout << "moved2" << std::endl;
    if (ui->pushButton_2->text() == "")
    {
        ui->pushButton_2->setText("Изменить");
        disconnect(ui->pushButton_2, SIGNAL(mouseMoved()), 0, 0);
    }
    disconnect(ui->pushButton_2, SIGNAL(clicked()), 0, 0);
    connect(ui->pushButton_2, SIGNAL(clicked()), this, SLOT(changeWindowState()));
}

void Form::changeWindowState()
{
    std::cout << "moved3" << std::endl;
    if (windowState() == Qt::WindowNoState)
        setWindowState(Qt::WindowMaximized);
    else
        setWindowState(Qt::WindowNoState);
}

void Form::resizeEvent(QResizeEvent*)
{
    if (!rect().intersects(ui->pushButton->geometry()))
        ui->pushButton->move(10, 10);
    if (!rect().intersects(ui->pushButton_2->geometry()))
        ui->pushButton_2->move(10, 40);
}
