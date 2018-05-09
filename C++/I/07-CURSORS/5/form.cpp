#include "form.h"
#include "ui_form.h"

#include <iostream>
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
    for (int i = 1; i < 3; i++)
    {
        str->push_back(QString("C%1").arg(i));
        cur->push_back(QCursor(QPixmap(QString(":/C%1.cur").arg(i))));
    }
    ui->pushButton_5->setTag(0);
    ico->push_back(style()->standardIcon(QStyle::SP_TitleBarMenuButton));
    ico->push_back(style()->standardIcon(QStyle::SP_ComputerIcon));
    ico->push_back(style()->standardIcon(QStyle::SP_DirIcon));
    setWindowIcon(ico->at(0));
    trayIcon->setIcon(ico->at(0));
    trayIcon->setToolTip("Icon in Traybar");
    trayIcon->setVisible(false);
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

void Form::on_pushButton_5_clicked()
{
    int k = (ui->pushButton_5->tag() + 1) % 3;
    ui->pushButton_5->setText(QString("Icon %1").arg(k));
    ui->pushButton_5->setTag(k);
    setWindowIcon(ico->at(k));
}

void Form::on_pushButton_6_clicked()
{
    bool b = ui->pushButton_6->text() == "Show Tray Icon";
    trayIcon->setVisible(b);
    ui->pushButton_6->setText(b ? "Hide Tray Icon" : "Show Tray Icon");
}
