#!/usr/bin/python3
"""
defines a square

Does value and type checks
"""


class Square:
    """Initialising size and giving error eceptions
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.position[1]):
                print('')

            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple or \
            len(position) != 2 or \
            not all(isinstance(el, int) for el in position) or \
                not all(el >= 0 for el in position):

            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position
