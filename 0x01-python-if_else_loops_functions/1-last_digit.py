#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    rm1 = -1 * ((-1 * number) % 10)
else:
    rm1 = number % 10
str1 = "Last digit of {} is {} and is ".format(number, rm1)
if rm1 == 0:
    print("{}0".format(str1))
elif rm1 > 5:
    print("{}greater than 5".format(str1))
else:
    print("{}less than 6 and not 0".format(str1))
