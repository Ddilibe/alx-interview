#!/usr/bin/python3
""" Script that addresses a challenge """
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
        Function that deteermines the fewest number of coins needed
        ro meet a given a total amount
        Args:
            :params: coins [List] - A list of possible combination
            :params: total [int] - Value to acquire from the combinations
        Return:
            This function returns an integer
    """
    value, new_sum = 0, 0
    if total == 0:
        return total
    new_coins = sorted(coins, reverse=True)
    for i in new_coins:
        while True:
            if (i + new_sum) < total:
                new_sum += i
                value += 1
            elif (new_sum + i) == total:
                return value + 1
            elif new_sum == total:
                return value
            else:
                break
    return -1
