#!/usr/bin/python3
""" Script that plays the prime game """


def get_prime(num: int) -> list:
    """
        Function that calculates the prime number under a certain number
        Args:
            :params: num[int] - Number to find the prime number under
        Return:
            A list containing the prime numbers
    """
    prime = []
    while num != 0:
        test, dam, nx = True, num, 0
        while True:
            nx += 1
            if nx > num:
                break
            if nx == num or nx == 1:
                continue
            elif (num % nx) == 0:
                test = False
        if test:
            prime.append(num)
        num -= 1
    prime.reverse()
    prime.remove(1)
    return prime


def isWinner(x: int, nums: list) -> [None or str]:
    """
        Function to determine the winner of a prime number game
        Args:
            :params: x[int] - The number of rounds to be played
            :params: nums[list] - The array containing n
        Return:
            This function returns a string or Nothing
    """
    rounds, ben, maria = [nums[i] for i in range(x)], [], []
    for i in range(x):
        play_game(ben, maria, rounds, nums, i)
    return winner(sum(ben), sum(maria))


def winner(ben: str, maria: str) -> [None or str]:
    """
        Function to declares the winner for the prime game
        Args:
            :params: ben[str] - Argument for the number of points ben has
            :params: maria[str] - Argument for the number of points maria has
        Return:
            This function returns a string value or nothing
    """
    if ben == maria:
        return None
    elif (ben > maria):
        return "Ben"
    else:
        return "Maria"


def play_game(ben: list, maria: list, rounds: list, nums: list, i) -> None:
    """
        Function for playing the major game
        Args:
            :params: ben[list] - Lists containing the score values for ben
            :params: maria[list] - Lists containing the score values for maria
            :params: rounds[list] - Lists containing the prime numbers to pick
            from
            :params: nums[list] - List containing the values to choose from
            :params: i[int] - Accounts for the round of the game present
        Return:
            This function does not return anything
    """
    value, nums, h = get_prime(rounds[i]), nums.copy(), 0
    return ben.append(1) if len(value) <= 0 else h
    for v in range(len(value)):
        multiples = [v*j for j in range(10000)]
        determine_multiples(value[v], nums, multiples)
    if v == 0 or v % 2 == 0:
        maria.append(1)
    else:
        ben.append(1)


def determine_multiples(i: int, nums: list, multiples: list) -> bool:
    """
        Function to get the multiples of a given number
        Args:
            :params: num[list] - Containing a list of numbers
            :params: multiples[list] - Containing a list of numbers
        Return:
            A boolean value either true or false
    """
    if i in nums:
        remove, value = [], True
        for i in nums:
            if i in multiples:
                remove.append(i)
        [nums.remove(i) for i in remove]
    else:
        value = False
    return value
