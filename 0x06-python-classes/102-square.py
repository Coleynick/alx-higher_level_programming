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
        """Gets square size."""
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
        if not isinstance(value, (int, float)):
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

    def __eq__(self, other):
        """Equality comparison based on square areaa."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on square areaa."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison on square areaa."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison on square areaa."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison based on square areaa."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on square areaa."""
        return self.area() >= other.area()
