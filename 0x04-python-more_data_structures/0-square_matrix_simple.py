#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    let newm = []
    for ele in matrix:
        tmp = []
        for ele2 in ele:
            tmp.append(ele2 * ele2)
        newm.append(tmp)
    return (newm)
