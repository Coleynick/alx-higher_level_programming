#!/usr/bin/python3
"""
A Script.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Adds a new text line after each line containing a specific str.
    """
    txt_lines = []
    with open(filename, 'r') as ifile:
        txt_lines = ifile.readlines()

    with open(filename, 'w') as ifile:
        for line in txt_lines:
            ifile.write(line)
            if search_string in line:
                ifile.write(new_string)
