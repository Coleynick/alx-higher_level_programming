#!/usr/bin/python3
"""
A Module.
"""


import json


def load_from_json_file(filename):
    """
    Create an obj from a JSON file.

    Args:
        filename (str): D name of the JSON file to load.

    Returns:
        object: The Python obj created from the JSON file.
    """
    with open(filename, "r") as ifile:
        return json.load(ifile)
