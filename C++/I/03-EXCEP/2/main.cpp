#include <QCoreApplication>
#include <iostream>
#include <limits>
#include <stdexcept>

using namespace std;

int ePow(int x, int y)
{
    int a = (int)pow(x, y);
    if (a == numeric_limits<int>::max())
    {
        throw overflow_error("Overflow Exception");
    }
    else if (a == numeric_limits<int>::min())
    {
        throw underflow_error("Underflow Exception");
    }
    return a;
}

int eDiv(int x, int y)
{
    if (y == 0)
    {
        throw runtime_error("DivideByZero Exception");
    }
    return x / y;
}

void M1(int x, int y, int z)
{
    try
    {
        int a = ePow(x, y);
        cout << (QString("x ^ y / z = %1").arg(eDiv(a, z))).toStdString() << endl;
    }
    catch (runtime_error e)
    {
        cout << e.what() << endl;
    }
    cout << "M1 finished" << endl;
}

void M2(int x, int y, int z)
{
    try
    {
        M1(x, y, z);
    }
    catch (overflow_error e)
    {
        cout << e.what() << endl;
    }
    catch (underflow_error e)
    {
        cout << e.what() << endl;
    }
    cout << "M2 finished" << endl;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    int x, y, z;
    try
    {
        cout << "x = ";
        if ((cin >> x).fail())
            throw invalid_argument("Format exception");
        cout << "y = ";
        if ((cin >> y).fail())
            throw invalid_argument("Format exception");
        cout << "x = ";
        if ((cin >> z).fail())
            throw invalid_argument("Format exception");
        M2(x, y, z);
    }
    catch (invalid_argument e)
    {
        cout << e.what() << endl;
    }
}
