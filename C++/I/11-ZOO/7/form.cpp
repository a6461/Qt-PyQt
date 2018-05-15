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
    DragDropLabel *src = (DragDropLabel*)event->source();
    src->move(event->pos());
}

void Form::reload()
{
    for (auto child = children().begin(); child < children().begin() + 4; child++)
    {
        std::string s = (*child)->objectName().toStdString().substr(5);
        auto *c = ui->horizontalLayoutWidget->findChild<DragDropLineEdit *>
                (QString::fromStdString("lineEdit" + s));
        QPoint pos = ui->horizontalLayoutWidget->mapToParent(c->pos());
        ((DragDropLabel*)(*child))->move(pos.x(), pos.y() / 2);
    }
    ui->pushButton->setFocus();
}

void Form::setButton()
{
    ui->pushButton->setText("Зоопарк открыт");
    ui->pushButton->setStyleSheet("color: green;");
    ui->pushButton->setIcon(
                style()->standardIcon(QStyle::SP_DialogApplyButton));
}

void Form::on_pushButton_clicked()
{
    reload();
    for (auto child = children().begin(); child < children().begin() + 4; child++)
    {
        ((DragDropLabel*)(*child))->setVisible(true);
        std::string s = (*child)->objectName().toStdString().substr(5);
        auto *c = ui->horizontalLayoutWidget->findChild<DragDropLineEdit*>
                (QString::fromStdString("lineEdit" + s));
        c->setText("");
        c->setTag(0);
    }
    ui->pushButton->setText("Зоопарк закрыт");
    ui->pushButton->setStyleSheet("color: red;");
    ui->pushButton->setIcon(
                style()->standardIcon(QStyle::SP_MessageBoxCritical));
}
