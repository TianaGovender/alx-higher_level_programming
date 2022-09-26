#!/usr/bin/python3
"""
Defines a Rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ REctangle class
    """
    def __init__(self, width, height):
        """area function

           Returns:
           an exception message
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """works out area
        """
        return (self__width * self.__height)

    def __str__(self):
        """print string
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)  
