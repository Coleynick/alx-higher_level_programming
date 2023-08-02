#!/usr/bin/python3
"""
Square module

defines Square class.
"""


class Square:
    """
    -

    Reps a square.

    Attributes:
        __size (intt): Size of square.
    """

    def __init__(self, size=0):
        """
        Initialize a Square with its parameters(size).

        Args:
            size (intt(optional)): Size of the square.

        Raises:
            TypeError & ValueError: If size is not an integer &
            If size is less than 0 respectivrly
        """
        self.size = size

    @property
    def size(self):
        """
        Gets square size.

        Returns:
            Size of the square(int).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set square size.

        Args:
            value (int): The new square size.

        Raises:
            TypeError & ValueError: If size is not an integer &
            If size is less than 0 respectivrly
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
             Current square area(int).
        """
        return self.__size ** 2
