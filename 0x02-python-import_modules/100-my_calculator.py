#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    length = len(argv) - 1

    if(length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if(op in ["+", "-", "*", "/"]):
        if(op == "+"):
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        else if(op == "-"):
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        else if(op == "*"):
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
            exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
