#ifndef FORM_H
#define FORM_H

#include <QSystemTrayIcon>
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
    void closeEvent(QCloseEvent *event);

private slots:
    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();

    void on_pushButton_6_clicked();

private:
    Ui::Form *ui;
    QList<QString> *str = new QList<QString>();
    QList<QCursor> *cur = new QList<QCursor>();
    QList<QIcon>* ico = new QList<QIcon>();
    QSystemTrayIcon *trayIcon = new QSystemTrayIcon();
};

#endif // FORM1_H
