#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Initialize the class.
        Args:
            size (int): The size of the class.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if not self.size:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.size)
