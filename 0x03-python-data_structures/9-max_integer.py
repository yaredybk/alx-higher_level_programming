#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list == 0)):
        return (None)
    val = my_list[0]
    for vv in my_list:
        if (vv > val):
            val = vv
    return (val)
