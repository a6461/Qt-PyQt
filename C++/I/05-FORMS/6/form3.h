#ifndef FORM3_H
#define FORM3_H

#include <QDialog>
#include <QPushButton>

namespace Ui {
class Form3;
}

class Form3 : public QDialog
{
    Q_OBJECT

public:
    explicit Form3(QWidget *parent = 0);
    ~Form3();

protected:
    void showEvent(QShowEvent*);

signals:
    void windowTitlesChanged(const QString &title1, const QString &title2);

private slots:
    void on_buttonBox_clicked(QAbstractButton *button);

private:
    Ui::Form3 *ui;
};

#endif // FORM3_H
