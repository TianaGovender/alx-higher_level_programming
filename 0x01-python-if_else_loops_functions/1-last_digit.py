#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n_str = repr(number)
last = int(n_str[-1])
if number < 0:
	last = -1 * last
if last > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, last))
if last < 6 and last != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last))
if last == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))