#include "form.h"
#include "ui_form.h"

#include <QMetaEnum>

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    setFixedSize(size());
    QMetaEnum metaEnum = QMetaEnum::fromType<Qt::CursorShape>();
    for (int cursor = Qt::ArrowCursor; cursor <= Qt::DragLinkCursor; cursor++)
    {
        str->push_back(metaEnum.valueToKey(cursor));
        cur->push_back(QCursor((Qt::CursorShape) cursor));
    }
    ui->pushButton->setTag(0);
}

Form::~Form()
{
    delete ui;
}

QList<QString>* Form::names()
{
    return str;
}

QList<QCursor>* Form::cursors()
{
    return cur;
}

void Form::on_pushButton_2_clicked()
{
    setCursor(ui->pushButton->cursor());
}

void Form::on_pushButton_3_clicked()
{
    setCursor(Qt::WaitCursor);
}

void Form::on_pushButton_4_clicked()
{
    setCursor(Qt::ArrowCursor);
}
