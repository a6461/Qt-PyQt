import os, sys, win32file
from PyQt5.QtCore import QStorageInfo

def DInfo(path):
    none = "---"
    d = path[0:2].upper()
    driveTypes = ["Unknown", "NoRootDirectory", "Removable", "Fixed",
                  "Remote", "CD-ROM", "RAM Drive"]
    driveType = win32file.GetDriveType(d)
    driveInfo = QStorageInfo(d)
    s = ' {:<4}'.format(d[0])
    if driveType != 1:
        s += ' {:<9}'.format(driveTypes[driveType])
        if driveInfo.isReady():
            s += '{:>12,} {:>12,}'.format(
                int(driveInfo.bytesTotal() / 1024),
                int(driveInfo.bytesFree() / 1024)).replace(",", " ")
        else:
            s += '{0:>12} {0:>12}'.format(none)
    else:
        s += ' {0:<9}{0:>12} {0:>12}'.format(none)
    print(s)
    
def main():
    print('Программа STORINFO\n')
    print(' Disk Type         Size (K)     Free (K)')
    print('=' * 40)
    DInfo(os.path.realpath(__file__))
    print('\nДля завершения программы нажмите <Enter>...')
    input()

if __name__ == '__main__':
    main()
