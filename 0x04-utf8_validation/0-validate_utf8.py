#!/usr/bin/python3
"""
Defines a method that determines if a given data set represents a valid UTF-8
encoding."""


def convert_to_binary(n):
    """returns a binary representation of an integer"""

    temp = []

    while n > 0:
        temp.append(n % 2)
        n = n // 2

    temp.reverse()

    if len(temp) < 8:
        binary = [0] * 8
        i = 8 - len(temp)

        for j in range(len(temp)):
            binary[i] = temp[j]
            i += 1

        binary = ''.join([str(ele) for ele in binary])
        return binary

    binary = ''.join([str(ele) for ele in temp])
    return binary


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding

    aargs
        data(list):  list of integers

    returns
        True if data is a valid UTF-8 encoding, else return False
    """
    for item in data:
        binary = convert_to_binary(item)
        if binary.startswith('10'):
            return False

    return True
