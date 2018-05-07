#include "form.h"
#include "ui_form.h"

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    setFixedSize(size());
    form2->setWindowFlags(Qt::Dialog | Qt::WindowMinMaxButtonsHint | Qt::WindowCloseButtonHint);
    form3->setWindowFlags(Qt::Dialog | Qt::WindowCloseButtonHint);
    connect(form2, SIGNAL(textChanged()), this, SLOT(changeButtonText()));
    connect(form3, SIGNAL(accepted()), this, SLOT(setWindowTitles()));
}

Form::~Form()
{
    delete ui;
}

void Form::on_pushButton_clicked()
{
    form2->move(geometry().right() - 10, geometry().bottom() - 10);
    emit form2->visibleChanged();
}

void Form::on_pushButton_2_clicked()
{
    form3->show();
}

void Form::changeButtonText()
{
    ui->pushButton->setText(form2->isVisible() ? "Закрыть подчиненное окно" :
        "Открыть подчиненное окно");
}

void Form::setWindowTitles()
{
    setWindowTitle(form3->mainWindowText());
    form2->setWindowTitle(form3->subWindowText());
}
