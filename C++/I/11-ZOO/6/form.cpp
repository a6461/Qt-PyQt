#include "form.h"
#include "ui_form.h"
#include "dragdroplabel.h"

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    setFixedSize(size());
    ui->label->setTag(3);
    ui->label_2->setTag(2);
    ui->label_3->setTag(1);
    ui->label_4->setTag(0);
    connect(ui->label, SIGNAL(buttonChanged()), this, SLOT(setButton()));
    connect(ui->label_2, SIGNAL(buttonChanged()), this, SLOT(setButton()));
    connect(ui->label_3, SIGNAL(buttonChanged()), this, SLOT(setButton()));
    connect(ui->label_4, SIGNAL(buttonChanged()), this, SLOT(setButton()));
    ui->pushButton->setIcon(
                style()->standardIcon(QStyle::SP_MessageBoxCritical));
}

Form::~Form()
{
    delete ui;
}

void Form::dragEnterEvent(QDragEnterEvent *event)
{
    event->accept();
}

void Form::dropEvent(QDropEvent *event)
{
    DragDropLabel *lb = (DragDropLabel*)event->source();
    lb->move(event->pos());
}

void Form::setButton()
{
    ui->pushButton->setText("Зоопарк открыт");
    ui->pushButton->setStyleSheet("color: green;");
    ui->pushButton->setIcon(
                style()->standardIcon(QStyle::SP_DialogApplyButton));
}
