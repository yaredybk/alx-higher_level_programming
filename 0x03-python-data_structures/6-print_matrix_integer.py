#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l1 in matrix:
        len1 = len(l1)
        for i in range(len1):
            print("{:d}".format(l1[i]))
            if (i == len1 -1):
                print("", end="\n")
            else:
                print(" ", end="")
