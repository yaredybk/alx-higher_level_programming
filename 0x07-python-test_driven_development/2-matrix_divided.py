#!/usr/bin/python3
"""
check if type is either integer or float
"""


def check_num(num):
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return True
    return False


"""
divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        ele = matrix[i]
        if not isinstance(ele, list):
            raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats")
        if (i == 0):
            ll = len(ele)
        else:
            if (ll != len(ele)):
                raise TypeError(
                        "Each row of the matrix must have the same size")
            else:
                ll = len(ele)
    if not check_num(div):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    new_mat = matrix.copy()
    for i in range(len(new_mat)):
        new_mat[i] = matrix[i].copy()
        for j in range(len(new_mat[i])):
            new_mat[i][j] = round(new_mat[i][j] / div, 2)
    return new_mat
