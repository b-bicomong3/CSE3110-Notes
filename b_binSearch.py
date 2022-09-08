"""
Title: Binary Search
Author: Beatrix Bicomong
Date: 06-09-2022
"""

from random import randrange
from time import perf_counter
from statistics import mean


def createArray(SIZE):
    """
    Create a random amount of numbers in an array, sorted
    :SIZE: int
    :return: LIST (int)
    """
    NUMBERS = []
    for i in range(2*SIZE):
        if randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS


def binarySearch(LIST, VALUE):
    """
    Search for a value within a LIST
    :param LIST: LIST (int)
    :param VALUE: (int)
    :return: (bool)
    """

    START = 0
    END = len(LIST) - 1

    while START <= END:
        MIDPOINT = (START + END) // 2 # Floor divide for an int
        if LIST[MIDPOINT] == VALUE:
            return True
        elif VALUE > LIST[MIDPOINT]:
            START = MIDPOINT + 1
        else:
            END = MIDPOINT - 1
    return False


if __name__ == "__main__":
    NUMBERS = createArray(10000000)

    TIMES = []
    for i in range(30):
        NUMBER = NUMBERS[randrange(len(NUMBERS))]
        print(NUMBER)

        START = perf_counter()
        FOUND = binarySearch(NUMBERS, NUMBER)
        END = perf_counter()

        print(FOUND)

        TIMES.append(END - START)

    print(mean(TIMES))

