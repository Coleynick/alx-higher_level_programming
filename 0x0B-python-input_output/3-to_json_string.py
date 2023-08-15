#!/usr/bin/python3
"""
A Module.
"""


import json


def to_json_string(my_obj):
    """
    Return the JSON rep.

    Args:
        my_obj: The obj to be converted to a JSON string.

    Returns:
        str: D JSON repr of obj.
    """
    return json.dumps(my_obj)
