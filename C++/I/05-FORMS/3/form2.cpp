#include "form2.h"
#include "ui_form2.h"

Form2::Form2(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Form2)
{
    ui->setupUi(this);
    connect(this, SIGNAL(visibleChanged()), this, SLOT(changeVisible()));
}

Form2::~Form2()
{
    delete ui;
}

void Form2::closeEvent(QCloseEvent *)
{
    setVisible(false);
    emit textChanged();
}

void Form2::changeVisible()
{
    setVisible(!isVisible());
    emit textChanged();
    if (isVisible())
        ui->label->setText(QString("Окно открыто в %1-й раз.").arg(++count));
}
