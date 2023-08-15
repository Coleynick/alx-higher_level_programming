#!/usr/bin/python3
"""
A Module.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an obj to a file withJSON.

    Args:
        my_obj: D Python object to be saved.
        filename (str): D name of the file.
    """
    with open(filename, "w") as ifile:
        json.dump(my_obj, ifile)
