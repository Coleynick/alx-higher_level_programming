#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elemnts of a matrix by a givn num.

    Args:
    matrix (list): A list of lists containing integers/floats.
    div (int or float): The number to divide the elements of the matrix.

    Returns:
    list: A new matrix, rounded to 2 decimal places.

    Raises:
    TypeError: If matrx != lis of lists of int/floats or if div is not a num.
    ZeroDivisionError: If div is == to 0.
    ValueError: If the rows of the matrix have diff sizes.

    Example:
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if not isinstance(matrix, list) \
            or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [
            [round(element / div, 2) for element in row]
            for row in matrix
            ]

    return new_matrix
