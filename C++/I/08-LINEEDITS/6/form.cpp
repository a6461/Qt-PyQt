#include "form.h"
#include "ui_form.h"
#include <QKeyEvent>

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    setFixedSize(size());
    ui->lineEdit->setFocus();
    connect(ui->radioButton_2, SIGNAL(toggled(bool)),
            this, SLOT(on_radioButton_toggled(bool)));
    setWindowFlags(Qt::Window | Qt::WindowContextHelpButtonHint | Qt::WindowCloseButtonHint);
}

Form::~Form()
{
    delete ui;
}

void Form::on_radioButton_toggled(bool checked)
{
    if (!checked)
        return;
    if (sender() == ui->radioButton)
    {
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 2; j++)
                setTabOrder(ui->gridLayout->itemAtPosition(i, j)->widget(),
                        ui->gridLayout->itemAtPosition(i, j + 1)->widget());
        for (int i = 0; i < 3; i++)
            setTabOrder(ui->gridLayout->itemAtPosition(i, 2)->widget(),
                    ui->gridLayout->itemAtPosition(i + 1, 0)->widget());
    }
    else
    {
        for (int j = 0; j < 3; j++)
            for (int i = 0; i < 3; i++)
                setTabOrder(ui->gridLayout->itemAtPosition(i, j)->widget(),
                        ui->gridLayout->itemAtPosition(i + 1, j)->widget());
        for (int j = 0; j < 2; j++)
            setTabOrder(ui->gridLayout->itemAtPosition(3, j)->widget(),
                    ui->gridLayout->itemAtPosition(0, j + 1)->widget());
    }
}

void Form::keyPressEvent(QKeyEvent *event)
{
    switch (event->key())
    {
        case Qt::Key_F2:
        {
            ui->radioButton->setChecked(true);
            break;
        }
        case Qt::Key_F3:
        {
            ui->radioButton_2->setChecked(true);
            break;
        }
    }
}

void Form::closeEvent(QCloseEvent *event)
{
    auto children = findChildren<QLineEdit*>();
    for (int i = 0; i < children.count(); i++)
    {
        if (((QLineEdit*)children[i])->actions().count() > 0)
        {
            event->ignore();
            return;
        }
    }
}
