#!/usr/bin/python3
"""
This module contains a function matrix_divided that divides all elements of a
matrix by a number.

The function takes two parameters: matrix and div. 
Matrix must be a list of lists of integers or floats, and div must be a number
(integer or float).
If either matrix or div does not meet these conditions, a TypeError exception
is raised.
If div is equal to 0, a ZeroDivisionError exception is raised.
The function returns a new matrix where all elements are divided by div,
rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix by a number.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The number to divide by.

    Returns:
    list of lists of int: The resulting matrix after division.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
