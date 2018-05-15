#include "form.h"
#include "ui_form.h"
#include "dragdroplabel.h"

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
	setFixedSize(size());
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
    auto trg = (DragDropLabel*)this->childAt(event->pos());
    if (!trg)
        event->accept();
    else
        event->ignore();
}

void Form::dropEvent(QDropEvent *event)
{
    DragDropLabel *src = (DragDropLabel*)event->source();
    src->move(event->pos());
}
