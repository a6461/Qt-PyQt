import os, sys, win32file
from PyQt5.QtCore import QStorageInfo
import psutil

def DInfo(path):
    none = "---"
    d = path[0:3].upper()
    #driveTypes = ["Unknown", "NoRootDirectory", "Removable", "Fixed",
    #              "Remote", "CD-ROM", "RAM Drive"]
    #driveType = win32file.GetDriveType(d)
    driveInfo = QStorageInfo(d)
    s = ' {:<4}'.format(d[0])
    for stor in psutil.disk_partitions():
        if stor.device == d:
            if os.name == 'nt':
                s += ' {:<9}'.format(stor.opts)
            else:
                s += ' {:<9}'.format(stor.fstype)
            if driveInfo.isReady():
                s += '{:>12,} {:>12,}'.format(
                    int(driveInfo.bytesTotal() / 1024),
                    int(driveInfo.bytesFree() / 1024)).replace(",", " ")
            else:
                s += '{0:>12} {0:>12}'.format(none)
        #else:
        #    s += ' {0:<9}{0:>12} {0:>12}'.format(none)
    print(s)
    
def main():
    print('Программа STORINFO\n')
    print(' Disk Type         Size (K)     Free (K)')
    print('=' * 40)
    #for stor in psutil.disk_partitions():
    #    print(stor.device, stor.opts)
    DInfo(os.path.realpath(__file__))
    print('\nДля завершения программы нажмите <Enter>...')
    input()

if __name__ == '__main__':
    main()
