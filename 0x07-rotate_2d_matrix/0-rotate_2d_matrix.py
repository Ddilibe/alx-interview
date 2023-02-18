#!/usr/bin/python3
""" Script that rotates a matrix at 90 degrees clockwise """


def rotate_2d_matrix(matrix) -> None:
    """
        Function for rotating a matrix 90 degress clockwise
        Args:
            :params: @matrix - A list of list containing the
            matrix to rotate
        Return:
            No return
    """
    old_matrix, n = matrix.copy(), len(matrix)
    for i in range(n):
        new_list = []
        for j in range(n):
            new_list.append(old_matrix[j][i])
        new_list.reverse()
        matrix[i] = new_list
