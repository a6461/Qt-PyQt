#include "form.h"
#include "ui_form.h"
#include <QMessageBox>

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

void Form::showEvent(QShowEvent*)
{
    int n = 7, nMax = 100001;
    QStringList args = QCoreApplication::arguments();
    if (args.count() > 1)
        try
        {
           int n0 = args.at(1).toInt();
           if (n0 < 2 || n0 > nMax)
               throw new std::exception();
           else
               n = n0;
        }
        catch (...)
        {
           QString s = QString("Неверный параметр: %1\nДопустимые значения: от 2 до %2").arg(args.at(1)).arg(nMax);
           QMessageBox(QMessageBox::Critical, "Ошибка", s).exec();
           close();
           return;
        }

    double step = 1.0 / (n - 1);
    ui->tableWidget->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
    ui->tableWidget->setRowCount(n);
    for (int i = 0; i < n; i++)
    {
        double x = i * step,
          sx = sin(M_PI * x),
          cx = cos(M_PI * x);
        ui->tableWidget->setItem(i, 0, new QTableWidgetItem(QString::number(x, 'f', 5)));
        ui->tableWidget->setItem(i, 1, new QTableWidgetItem(QString::number(sx)));
        ui->tableWidget->setItem(i, 2, new QTableWidgetItem(QString::number(cx)));
        ui->tableWidget->setItem(i, 3, new QTableWidgetItem(QString::number(sx / cx)));
        ui->tableWidget->setItem(i, 4, new QTableWidgetItem(QString::number(cx / sx)));
    }
}
