#!/usr/bin/python3
""" Script for the island perimeter """


def confirm_boundary(grid: list, i: int, j: int, point: list) -> None:
    """
        Function to confirm whether the sides of a square is boundarying
        another square or water
        Args:
            :params: grid[list] - A list of list containing the 2-d
            visualized space with ones representing land and zeros
            representing water
            :params: i[int] - An integer parameter used to access the
            vertical part of the 2-D list of list
            :params: j[int] - An integer parameter used to access the
            horizontal part of the 2-D list of list
            :params: point[list] - A list of integers containing the number
            of sides to the square once gotten
        Return:
            There is no return value
    """
    variables = [(i-1, j), (i, j+1), (i, j-1), (i+1, j)]
    for values in variables:
        try:
            if grid[values[0]][values[1]] == 0:
                point.append(1)
        except Exception as e:
            pass


def island_perimeter(grid):
    """
        Function for calculating the perimeter for a gird
        Args:
            :params: grid[list of list] - A list of list
        Return:
            This would return an interger which is the
            perimeter of the grid
    """
    if grid == []:
        return 0
    r, l, num = len(grid), len(grid[0]), []
    for i in range(r):
        for j in range(l):
            if grid[i][j] == 1:
                confirm_boundary(grid, i, j, num)
    return sum(num)
