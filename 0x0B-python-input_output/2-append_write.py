#!/usr/bin/python3
"""
A Module.
"""


def append_write(filename="", text=""):
    """
    Add a str to the end of a file.

    Args:
        filename (str): D name of the file.
        text (str): The str to be appended to the file.

    Returns:
        int: The num of char added.
    """
    with open(filename, 'a', encoding='utf-8') as ifile:
        return ifile.write(text)
