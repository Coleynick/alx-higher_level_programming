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
            size (intt): Size of the square.
        """
        self.__size = size
