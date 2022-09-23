#!/usr/bin/python3
"""Defines an integer addition function"""

def add_integer(a, b=98):
    """Return addition

       Raises:
       TypeError: If either a or b is not an int or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("a must be an integer")
    return (int(a) + int(b))
