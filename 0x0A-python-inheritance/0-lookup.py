#!/usr/bin/python3
"""A module for LOOKUP function."""


def lookup(obj):
    """
    Returns a lis of availa-ble attr and methods of an obj.

    Args:
        obj

    Returns:
        list
    """
    return dir(obj)
