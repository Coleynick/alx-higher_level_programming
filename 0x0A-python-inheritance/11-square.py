#!/usr/bin/python3
""" A module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Inits a Square instance.

        Args:
            size (int): square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a str rep of the squa.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
