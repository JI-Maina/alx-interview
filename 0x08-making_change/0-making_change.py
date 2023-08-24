#!/usr/bin/python3
"""Defines a function that determines the fewest number of coins needed
to meet a given amount
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num = 0
    for item in coins:
        while total >= item:
            total = total - item
            num += 1

        if total == 0:
            break

    if total > 0:
        return -1
    return num
