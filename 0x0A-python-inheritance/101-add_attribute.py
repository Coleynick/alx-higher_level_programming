#!/usr/bin/python3
""" A module """


def add_attribute(obj, attribute, value):
    """
    Add a new attr to an object if poss.

    Args:
        obj: The obj to which the attr will be added.
        attribute: The name of the attr to add.
        value: The val of the new att.

    Returns:
        None

    Raises:
        TypeError: If obj cannot have new attr.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
