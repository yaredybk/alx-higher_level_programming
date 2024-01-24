#!/usr/bin/python3
for letter in range(1, 27):
    if (letter % 2 == 1):
        x = 96
    else:
        x = 64
    letter = 27 - letter + x
    print("{}".format(chr(letter)), end="")
