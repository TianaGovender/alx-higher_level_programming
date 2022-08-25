#!/usr/bin/python3
import sys

len = (len(sys.argv) - 1)
if len == 0:
   print("0 arguments.")
if len == 1:
   print("{} argument:".format(len))
if len > 1:
   print("{} arguments:".format(len))

i = 1
while i <= len:
   print("{}: {}".format(i, sys.argv[i]))
   i = i + 1;
