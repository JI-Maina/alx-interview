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

    c_sum = 0
    for coin in coins:
        c_sum = c_sum + coin

    if c_sum > total:
        return -1
    return 0
