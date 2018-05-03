#include "form.h"
#include "ui_form.h"
#include "dragdroplabel.h"

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

void Form::dragEnterEvent(QDragEnterEvent *event)
{
    event->accept();
}

void Form::dragMoveEvent(QDragMoveEvent *event)
{
    auto child = (DragDropLabel*)this->childAt(event->pos());
    if (!child || child == event->source())
        event->accept();
    else
        event->ignore();
}

void Form::dropEvent(QDropEvent *event)
{
    DragDropLabel *lb = (DragDropLabel*)event->source();
    lb->move(event->pos());
}
