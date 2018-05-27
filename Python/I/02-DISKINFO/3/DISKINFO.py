import os, sys, win32file
from PyQt5.QtCore import QStorageInfo

def driveTypes():
    types = {}
    for value in dir(win32file):
        if value[0:6] == 'DRIVE_':
            key = getattr(win32file, value)
            types[key] =  value[6:]
    types = [value for (key, value) in sorted(types.items())]
    return types

def DInfo(path):
    none = "---"
    d = path[0:3].upper()
    si = QStorageInfo(d)
    s = ' {:<4}'.format(d[0])
    dt = driveTypes()
    if si.isValid():
        if os.name == 'nt':
            s += ' {:<12}'.format(dt[win32file.GetDriveType(d)])
        else:
            s += ' {:<12}'.format(none)
        if si.isReady():
            s += '{:>12,} {:>12,}'.format(
                int(si.bytesTotal() / 1024),
                int(si.bytesFree() / 1024)).replace(",", " ")
        else:
            s += '{0:>12} {0:>12}'.format(none)
    else:
        s += ' {0:<12}{0:>12} {0:>12}'.format(none)
    print(s)
    
def main():
    print('Программа DISKINFO\n')
    print(' Disk Type         Size (K)     Free (K)')
    print('=' * 43)
    if len(sys.argv) < 2:
        DInfo(os.path.realpath(__file__))
    else:
        for d in sys.argv[1:]:
            DInfo(d + ':/')
    print('\nДля завершения программы нажмите <Enter>...')
    input()

if __name__ == '__main__':
    main()
