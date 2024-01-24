#!/usr/bin/python3
def no_c(my_string):
    tmp = ""
    for i in range(len(my_string)):
        char = my_string[i]
        if (char != 'c' and char != 'C'):
            tmp = tmp.join(char)
    return (tmp)
