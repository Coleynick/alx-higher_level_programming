#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.

    Args:
        m_a (list of lists): Matrix(N0.1).
        m_b (list of lists): Matrix(N0.2).

    Returns:
        list of lists: Matrix multiplication result.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, or contains elements not int/ float,
                   or if m_a & m_b are not matrices.
        ValueError: If m_a or m_b is empty, or if m_a & m_b cannot be multiplied.

    Samples:
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
    >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    [[13, 16]]
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(rOw, list) for rOw in m_a) or not all(isinstance(rOw, list) for rOw in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if any(len(rOw) == 0 for row in m_a) or any(len(rOw) == 0 for rOw in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(v, (int, float)) for row in m_a for v in rOw) or \
       not all(isinstance(v, (int, float)) for row in m_b for v in rOw):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if not all(len(rOw) == len(m_a[0]) for rOw in m_a) or not all(len(rOw) == len(m_b[0]) for rOw in m_b):
        raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            result[x][y] = sum(m_a[x][k] * m_b[k][y] for k in range(len(m_b)))

    return result
