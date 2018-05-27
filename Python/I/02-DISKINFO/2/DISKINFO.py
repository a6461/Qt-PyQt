import os, win32file
from PyQt5.QtCore import QStorageInfo

def driveTypes():
    types = []
    for value in dir(win32file):
        if value[0:6] == 'DRIVE_':
            types.append(value[6:].lower().title())
    return types

def DInfo(path):
    none = "---"
    d = path[0:3].upper()
    si = QStorageInfo(d)
    s = ' {:<4}'.format(d[0])
    dt = driveTypes()
    if si.isValid():
        if os.name == 'nt':
            s += ' {:<11}'.format(dt[win32file.GetDriveType(s)])
        else:
            s += ' {:<11}'.format(none)
        if si.isReady():
            s += '{:>12,} {:>12,}'.format(
                int(si.bytesTotal() / 1024),
                int(si.bytesFree() / 1024)).replace(",", " ")
        else:
            s += '{0:>12} {0:>12}'.format(none)
    else:
        s += ' {0:<11}{0:>12} {0:>12}'.format(none)
    print(s)
    
def main():
    print('Программа DISKINFO\n')
    print(' Disk Type         Size (K)     Free (K)')
    print('=' * 42)
    DInfo(os.path.realpath(__file__))
    print('\nДля завершения программы нажмите <Enter>...')
    input()

if __name__ == '__main__':
    main()
