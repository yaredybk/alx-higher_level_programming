#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newl = []
    for ele in my_list:
        newl.append((ele % 2) == 0)
    return (newl)
