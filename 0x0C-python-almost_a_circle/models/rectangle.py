#!/usr/bin/python3
"""
Defines rectangle
"""


class Rectangle(Base):
    """Implementations
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Defines the instances
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """get width of Rec"""
        return self.__width


    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get width of rec"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        "get x"
        return self.__x

    @x.setter
    def x(self, value):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """finds area of rec"""
        return (self.__height * self.__width)

    def display(self):
        """prints rec"""
        for i in range(self.__width):
            print("#" * height)

