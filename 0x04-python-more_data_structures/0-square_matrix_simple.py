#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = matrix.copy()
    for ind in range(len(matrix) - 1):
        for ind2 in range(len(matrix[ind]) - 1):
            ele2 = matrix[ind][ind2]
            newm[ind][ind2] = (ele2 * ele2)
    return (newm)
