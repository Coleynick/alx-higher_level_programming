#!/usr/bin/python3
"""
A Module.
"""


def write_file(filename="", text=""):
    """
    Write a str to a file.

    Args:
        filename (str): D name of the text file.
        text (str): D str to be written to file.

    Returns:
        int: The num of char written.

    """
    with open(filename, 'w', encoding='utf-8') as ifile:
        return ifile.write(text)
