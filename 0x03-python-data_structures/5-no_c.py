#!/usr/bin/python3
def no_c(my_string):
    tmp = ""
    for i in range(len(my_string)):
        char = my_string[i]
        if (char != 'c' or char != 'C'):
            tmp += char
    return (tmp)
