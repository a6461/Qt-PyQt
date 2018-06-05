#include <QCoreApplication>
#include <QStorageInfo>
#include <QStringList>
#include <QTextCodec>
#include <iostream>

#ifdef Q_OS_WIN32
#include <windows.h>
#endif

using namespace std;

void DInfo(QString path)
{
    QString none("---");
    QString d = path.mid(0, 3);
    QStorageInfo *si = new QStorageInfo(d);
    QString s = QString(" %1").arg(d[0], -4);
    QStringList dt = { "UNKNOWN", "NO_ROOT_DIR", "REMOVABLE", "FIXED", "REMOTE", "CDROM", "RAMDISK" };
    if (si->isValid())
    {
        #ifdef Q_OS_WIN32
            s.append(QString(" %1").arg(dt.at(GetDriveType((wchar_t*)d.utf16())), -12));
        #else
            s.append(QString(" %1").arg(none, -4));
        #endif
        if (si->isReady())
            s.append(QString("%L1 %L2").arg(si->bytesTotal() / 1024, 12).arg(si->bytesFree() / 1024, 12));
        else
            s.append(QString("%1 %2").arg(none, 12).arg(none, 12));
    }
    else
        s.append(QString(" %1%2 %3").arg(none, -12).arg(none, 12).arg(none, 12));
    cout << s.toLocal8Bit().data() << endl;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

#ifdef Q_OS_WIN32
    QTextCodec::setCodecForLocale(QTextCodec::codecForName("IBM 866"));
#else
    QTextCodec::setCodecForLocale(QTextCodec::codecForName("UTF-8"));
#endif

    cout << QString("Программа DISKINFO\n").toLocal8Bit().data() << endl;
    cout << QString(" Disk Type            Size (K)     Free (K)\n").toStdString();
    cout << QString(43, '=').toStdString() << endl;
    DInfo(a.applicationFilePath());
    cout << QString("\nДля завершения программы нажмите <Enter>...").toLocal8Bit().data() << endl;
}
