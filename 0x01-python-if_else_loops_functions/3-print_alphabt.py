#!/usr/bin/python3
for i in range(97, 123):
    if i not in (101, 113):
        print("{0:c}".format(i), end="")
