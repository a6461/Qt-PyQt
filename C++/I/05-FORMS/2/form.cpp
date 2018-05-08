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
    connect(form2, SIGNAL(visibleChanged(bool)), this, SLOT(setPushButtonText(bool)));
}

Form::~Form()
{
    delete ui;
}

void Form::on_pushButton_clicked()
{
    form2->move(geometry().right() - 10, geometry().bottom() - 10);
    if (form2->isVisible())
        form2->close();
    else
        form2->show();
}

void Form::on_pushButton_2_clicked()
{
    form3->show();
}

void Form::setPushButtonText(bool visible)
{
    ui->pushButton->setText(visible ? "Открыть подчиненное окно" :
        "Закрыть подчиненное окно");
}
