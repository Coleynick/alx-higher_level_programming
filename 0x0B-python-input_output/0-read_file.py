#!/usr/bin/python3
"""
A Module.
"""


def read_file(filename=""):
    """
    Read and print contents of a file.

    Args:
        filename (str): D name of the text file.

    """
    with open(filename, 'r', encoding='utf-8') as ifile:
        print(ifile.read(), end="")
