#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n_str = repr(number)
last = int(n_str[-1])
if number < 0:
    last = -1 * last
print("Last digit of {} is {}".format(number, last), end='')
if last > 5:
    print("and is greater than 5")
if last < 6 and last != 0:
    print("and is less than 6 and not 0")
if last == 0:
    print("and is 0")
