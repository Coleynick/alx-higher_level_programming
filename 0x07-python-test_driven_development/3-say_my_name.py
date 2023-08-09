#!/usr/bin/python3
"""Module to say the name
"""


def say_my_name(first_name, last_name=""):
    """Print d name in a specific format

    Args:
        first_name (str): 1st name.
        last_name (str, optional): D Last name.

    Raises:
        TypeError: If first_name or last_name is not a str.

    Returns:
        str: Str formatted name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        return "My name is {} {}".format(first_name, last_name)
    else:
        return "My name is {}".format(first_name)
