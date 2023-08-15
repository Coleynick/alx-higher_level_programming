#!/usr/bin/python3
"""
A Module.
"""


import json


def from_json_string(my_str):
    """
    Return the python data struct.

    Args:
        my_obj: The json to be converted.

    Returns:
        str: D python data struct.
    """
    return json.loads(my_str)
