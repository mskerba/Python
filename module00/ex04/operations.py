import sys

def Sum(a, b):
    a += b
    print("Sum:         " + str(a))

def Difference(a, b):
    a -= b
    print("Difference:  " + str(a))

def Product(a, b):
    a *= b
    print("Product:     " + str(a))

def Quotient(a, b):
    if b == 0:
        print("Quotient:    ERROR (division by zero)")
    else:
        a /= b
        print("Quotient:    " + str(a))

def Remainder(a, b):
    if b == 0:
        print("Remainder:   ERROR (modulo by zero)")
    else:
        a %= b
        print("Remainder:   " + str(a))

def operation(a, b):
    Sum(a, b)
    Difference(a, b)
    Product(a, b)
    Quotient(a, b)
    Remainder(a, b)


if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("AssertionError: too many arguments")
    elif len(sys.argv) < 3:
        print("Usage: python operations.py <number1> <number2>")
        print("Example:")
        print("python operations.py 10 3")
    elif sys.argv[1].isdigit() and sys.argv[2].isdigit():
        operation(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("AssertionError: only integers")

    
