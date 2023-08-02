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
        __position (tuple): The square position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square with its parameters(size).

        Args:
            size (intt(optional)): Size of the square.

        Raises:
            TypeError & ValueError: If size is not an integer &
            If size is less than 0 respectivrly
        """
        self.size = size
        self.position = position

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

    @position.setter
    def position(self, value):
        """Sets square position.

        Args:
            value (tuple): Square position.

        Raises:
            TypeError: If position is not a tuple of 2 +(positive) integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        a, b = value
        if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
             Current square area(int).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print square using the character '#'.

        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        else:
            for a in range(self.__position[1]):
                print()
            for a in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
