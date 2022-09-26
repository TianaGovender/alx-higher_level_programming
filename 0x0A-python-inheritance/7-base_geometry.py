#!/usr/bin/python3
"""
Defines a BaseGeometry class
"""


class BaseGeometry:
    """ Mylist class
    """
    def area(self):
        """area function

           Returns:
           an exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate int

           Args:
               name: is string
               value: is an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater then 0".format(name))
