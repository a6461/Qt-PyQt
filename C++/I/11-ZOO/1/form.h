#ifndef FORM_H
#define FORM_H

#include <QDragEnterEvent>
#include <QDragMoveEvent>
#include <QDropEvent>
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
    void dragEnterEvent(QDragEnterEvent *event);
    void dragMoveEvent(QDragMoveEvent *event);
    void dropEvent(QDropEvent *event);

private:
    Ui::Form *ui;
};

#endif // FORM_H
