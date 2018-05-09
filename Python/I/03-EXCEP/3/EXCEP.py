import logging

def M1(x, y, z):
    try:
        a = pow(x, y)
        print("x ^ y / z = %d" % (a / z))
    except ZeroDivisionError as e:
        print("ZeroDivision Exception")
    print("M1 finished")
    
def M2(x, y, z):
    try:
        M1(x, y, z)
    except ArithmeticError:
        print("Arithmetic Exception")
        raise
    print("M2 finished")
    
def main():
    try:
        x = int(input("x = "))
        y = int(input("y = "))
        z = int(input("z = "))
        M2(x, y, z)
    except Exception as e:
        logging.Logger('catch_all').exception(e, exc_info=False)
    input()
    
if __name__ == "__main__":
    main()
