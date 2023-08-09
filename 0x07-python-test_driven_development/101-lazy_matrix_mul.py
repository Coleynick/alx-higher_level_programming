#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by NumPy.

    Args:
        m_a (list of lists): Matrix (No. 1).
        m_b (list of lists): Matrix (No. 2).

    Returns:
        list of lists: Matrix multiplication result.
    """
    return np.matmul(m_a, m_b)
