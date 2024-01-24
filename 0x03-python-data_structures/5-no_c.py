#!/usr/bin/python3
def no_c(my_string):
    for i in range(my_string):
        char = my_string[i]
        if (char == 'c' or char == 'C'):
            my_string = my_string[:i] + my_string[(i+1):]
    return (my_string)
