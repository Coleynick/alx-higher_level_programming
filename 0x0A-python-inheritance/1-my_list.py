#!/usr/bin/python3
"""
A module.
"""


class MyList(list):
    """
    MyList class, inherits from list.
    """
    def print_sorted(self):
        """
        Prints the sorted list in ascending order.
        """
        print(sorted(self))
