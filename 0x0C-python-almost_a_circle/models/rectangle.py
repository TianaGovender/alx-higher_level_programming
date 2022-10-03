#!/usr/bin/python3
"""
Defines rectangle
"""
from models.base import Base

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
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for j in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

     def __str__(self):
         """print statement"""
         return "[Rectangle] {} {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

     def update(self, *args, **kwargs):
         """Update The Rec"""
         if args and len(args) != 0:
             a = 0
             for i in args:
                 if a == 0:
                     if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                     else:
                        self.id = i
                 elif a == 1:
                     self.width = i
                 elif a == 2:
                     self.height = i
                 elif a == 3:
                     self.x = i
                 elif a == 4:
                     self.y = i
                 a += 1

          elif kwargs and len(kwargs) != 0:
              for k, v in kwargs.items():
                  if k == "id":
                      if v is None:
                          self.__init__(self.width, self.heigth, self.x, self.y)
                      else:
                          self.id = v
                  elif k == "width":
                      self.width = v
                  elif k == "height":
                      self.height = v
                  elif k == "x":
                      self.x = v
                  elif k == "y":
                      self.y = v

      def to_dictionary(self):
          """dic rep of rec"""
          return {
              "id": self.id,
              "width": self.width,
              "heigth": self.height,
              "x": self.x,
              "y": self.y
          }
