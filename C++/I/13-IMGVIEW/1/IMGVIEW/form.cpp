#include "form.h"
#include "ui_form.h"
#include <QFileSystemModel>
#include <iostream>

Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    ui->treeView->setMinimumWidth(ui->treeView->width());
    ui->listWidget->setMinimumWidth(ui->listWidget->width());
    QFileSystemModel *model = new QFileSystemModel;
    model->setRootPath(QDir::currentPath());
    model->removeColumns(1, 3);
    std::cout << model->columnCount() << std::endl;
    ui->treeView->setModel(model);
    //ui->treeView->header()->hide();
    ui->treeView->header()->setStretchLastSection(true);
}

Form::~Form()
{
    delete ui;
}
