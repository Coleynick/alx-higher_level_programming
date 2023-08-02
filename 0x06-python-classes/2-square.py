#!/usr/bin/python3
"""
Square module -

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
