#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """An n x n 2D matrix, rotate it
    90 degrees clockwise"""
    Len = len(matrix[0])
    for i in range(Len // 2):
        for j in range(i, Len - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[Len - 1 - j][i]
            matrix[Len - 1 - j][i] = matrix[Len - 1 - i][Len - 1 - j]
            matrix[Len - 1 - i][Len - 1 - j] = matrix[j][Len - 1 - i]
            matrix[j][Len - 1 - i] = temp
