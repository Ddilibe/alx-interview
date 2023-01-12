#!/usr/bin/python3
""" Script that tests and visualizes minimum operations """


def minOperations(n: int) -> int:
    """
        Function to determine the minimum operation over the duplication of a
        certain string

        Args:
            :param n [int] - The first argument

        Return:
            This function returns an integer as a value
    """
    if n == 2:
        return 1
    if n == 1:
        return 0
    if n == 3:
        return 3
    if n == 4:
        return 4
    i, h = 2, "H"
    while True:
        if n % i == 0:
            break
        i += 1
    first = int(n/i) + i
    i, h = 3, "H"
    while True:
        if n % i == 0:
            break
        i += 1
    second = int(n/i) + i
    if first < second:
        return first
    return second
