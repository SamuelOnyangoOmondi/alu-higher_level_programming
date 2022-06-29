#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    modulo = number % 10
else:
    modulo = number % -10
str1 = " and is greater than 5"
str2 = " and is less than 6 and not 0"
if modulo > 5:
    print("Last digit of {:d} is {:d}".format(number, modulo) + str1)
elif modulo == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, modulo))
else:
    print("Last digit of {:d} is {:d}".format(number, modulo) + str2)
