#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if (len(argv) == 1):
        print("{:d}".format(0))
    else:
        summ = 0
        for i in range(1, len(argv)):
            summ += int(argv[i])
        print("{:d}".format(summ))
