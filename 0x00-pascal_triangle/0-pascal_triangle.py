#!/usr/bin/python3

"""
Script that demonstrates the pascal's triangle
"""


def pascal_triangle(n):
    """
        Function for creating the pascal's triangle

        Arguments:
            n: Integer variable in the triangle

        Return:
            List if n > 0
            empty list if n <= 0
    """
    i, other = 0, []
    while i < n:
        y, tri = 0, []
        while y <= i:
            tri.append(combination(i, y))
            y += 1
        other.append(tri)
        i += 1
    return other


def combination(x: int, y: int) -> int:
    """
        Function used for recreating the combination

        Arguments:
            x: First integer
            y: Second integer

        Return:
            Combination of the integer
    """
    i, j, k = 1, 1, 1
    for w in range(1, x+1):
        i *= w
    for w in range(1, (x - y) + 1):
        j *= w
    for w in range(1, y+1):
        k *= w
    ans = (i)/(j * k)
    return int(ans)
