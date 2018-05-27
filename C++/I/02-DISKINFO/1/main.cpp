#include <QCoreApplication>
#include <QTextCodec>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

#ifdef Q_OS_WIN32
    QTextCodec::setCodecForLocale(QTextCodec::codecForName("IBM 866"));
#endif

#ifdef Q_OS_LINUX
    QTextCodec::setCodecForLocale(QTextCodec::codecForName("UTF-8"));
#endif

    std::cout << QString("Программа DISKINFO\n").toLocal8Bit().data() << std::endl;
    std::cout << QString("\nДля завершения программы нажмите <Enter>...").toLocal8Bit().data() << std::endl;
}
