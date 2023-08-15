#!/usr/bin/python3
"""A module """


class MyInt(int):
    """
    An integer class.
    """

    def __eq__(self, other):
        """
        Check if not equal.

        Args:
            other: compare with.

        Returns:
            bool: True != equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Check if two MyInt are equal.

        Args:
            other: compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
