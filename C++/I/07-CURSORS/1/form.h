#ifndef FORM_H
#define FORM_H

#include <QWidget>

namespace Ui {
class Form;
}

class Form : public QWidget
{
    Q_OBJECT

public:
    explicit Form(QWidget *parent = 0);
    ~Form();
    QList<QString>* names();
    QList<QCursor>* cursors();

private:
    Ui::Form *ui;
    QList<QString> *str = new QList<QString>();
    QList<QCursor> *cur = new QList<QCursor>();
};

#endif // FORM_H
