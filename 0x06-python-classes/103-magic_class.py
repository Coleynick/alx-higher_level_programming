#!/usr/bin/python3
import math
import dis


class MagicClass:
    """Reps a magic class that calculates area and circumference of a circle.

    Attributes:
        __radius (float): The circle radius.
    """

    def __init__(self, radius=0):
        """Initializes MagicClass with its parameter(razdius).

        Args:
            radius (float): Circle radius.

        Raises:
            TypeError: If the radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    def area(self):
        """Calculates the area of the circle.

        Returns:
            float: The circle area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates circle circumferenece.

        Returns:
            float: Circle circumference.
        """
        return 2 * math.pi * self.__radius
