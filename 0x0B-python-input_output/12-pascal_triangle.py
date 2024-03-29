#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.

    Parameters:
    n (int): The number of rows in Pascal's triangle.

    Returns:
    list: A list of lists where each list
    represents a row in Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[i - 1]
        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
