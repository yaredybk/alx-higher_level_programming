#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (len(my_list) > 0):
        for i in range(len(my_list)):
            i = len(my_list) - i - 1
            print("{:d}".format(my_list[i]))
