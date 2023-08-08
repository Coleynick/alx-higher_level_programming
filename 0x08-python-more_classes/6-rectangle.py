#!/usr/bin/python3
""" A module containing the dfeinition of an empty string """


class Rectangle:
    """
    Reps a rectangle.

    Attributes:
        width (int): Rectangle width.
        height (int): Rectangle height.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with this given width and height.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.

        Raises:
            ValueError: If width or height is below 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width.

        Args:
            value(int): Rectangle width.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is below 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height.

        Args:
            value(int): The rectangle height.

        Raises:
            TypeError: If height is not an int.
            ValueError: If height is below 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate rectangle area.

        Returns:
            Rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate rectangle perimeter.

        Returns:
            Rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """String repr of rectangle using '#'.

        Returns:
            str: Rectangle string representation.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_str = ""
        for a in range(self.__height):
            rec_str += "#" * self.__width + "\n"
        return rec_str.strip()

    def __repr__(self):
        """Rec string representation that can be used with eval().

        Returns:
            str: Rectangle string representation.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a goodbye mssg when the instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
