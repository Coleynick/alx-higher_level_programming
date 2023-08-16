#!/usr/bin/python3
"""
A module.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.
    """
    if n <= 0:
        return []

    tri = [[1]]

    for i in range(1, n):
        pas_row = tri[i - 1]
        add_row = [1]
        for j in range(1, i):
            add_row.append(pas_row[j - 1] + pas_row[j])
        add_row.append(1)
        tri.append(add_row)
    return tri
