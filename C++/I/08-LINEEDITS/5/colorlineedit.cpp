#include "colorlineedit.h"
#include <QAction>
#include <QApplication>
#include <QKeyEvent>
#include <QStyle>
#include <iostream>

ColorLineEdit::ColorLineEdit(QWidget *parent):
   QLineEdit(parent)
{
    connect(this, SIGNAL(textChanged(QString)), this, SLOT(on_textChanged()));
}

void ColorLineEdit::focusInEvent(QFocusEvent *)
{
    setStyleSheet("background-color: darkGreen; color: white");
    selectAll();
    QApplication::sendEvent(this, new QKeyEvent(QEvent::KeyPress, Qt::Key_Right, Qt::NoModifier));
    deselect();
}

void ColorLineEdit::focusOutEvent(QFocusEvent *)
{
    selectAll();
    deselect();
    setStyleSheet("background-color: Window; color: WindowText");
    if (text().trimmed() == "")
        setFocus();
}

void ColorLineEdit::on_textChanged()
{
    if (actions().count() > 0)
        removeAction(actions().at(0));
    if (text().trimmed() == "")
        if (actions().count() == 0)
        {
            QAction *action = new QAction(QIcon(style()->standardPixmap(QStyle::SP_MessageBoxCritical)), "");
            action->setWhatsThis("Текст в поле ввода не должен быть пустым.");
            addAction(action, QLineEdit::TrailingPosition);
            setFixedWidth(width());
        }
}
