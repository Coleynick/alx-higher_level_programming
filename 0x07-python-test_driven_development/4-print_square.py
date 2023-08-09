#!/usr/bin/python3
def print_square(size):
    """
    Prints a square made of '#' chars.

    Args:
    size (int): The square size length.

    Raises:
    TypeError: If size is != int.
    ValueError: If size is below 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
