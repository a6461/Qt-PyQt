def M1(x, y, z):
    try:
        a = pow(x, y)
        print('x ^ y / z = %d' % (a / z))
    except ZeroDivisionError as e:
        print('ZeroDivision Exception')
    print('M1 finished')
    
def M2(x, y, z):
    try:
        M1(x, y, z)
    except ArithmeticError:
        print('Arithmetic Exception')
    print('M2 finished')
    
def main():
    x = int(input('x = '))
    y = int(input('y = '))
    z = int(input('z = '))
    M2(x, y, z)
    input()
    
if __name__ == '__main__':
    main()
