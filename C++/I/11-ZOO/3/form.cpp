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
    DragDropLabel *src = (DragDropLabel*)event->source();
    src->move(event->pos());
}
