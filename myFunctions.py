# myFunctions.py
"""
Title: Common functions
Author: Beatrix Bicomong
Date-created: 08-09-2022
"""
import random, time, statistics


def getSmalllist():
    """
    return small mixed list of integers
    :return: list (int)
    """
    return [1, 5, 19, 1, 11, 17, 7, 13]


def getList(SIZE):
    """
    returns a sorted list of approximately size SIZE
    :param SIZE: int
    :return: list (int)
    """
    NUMBERS = []
    for i in range(2 * SIZE):
        if random.randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS


def getRandomList(SIZE):
    """
    returns a randomized list of approximately size SIZE
    :param SIZE: int
    :return: list (int)
    """
    SORTED_LIST = getList(SIZE)
    RANDOM_LIST = []
    for i in range(len(SORTED_LIST)):
        RANDOM_LIST.append(SORTED_LIST.pop(random.randrange(len(SORTED_LIST))))

    return RANDOM_LIST


def getAverage(TIMES):
    """
    returns the average of the given list
    :param TIMES: list (float)
    :return: float
    """
    return statistics.mean(TIMES)


def getTime():
    """
    returns the performance counter
    :return: float
    """
    return time.perf_counter()


if __name__ == "__main__":
    print(getSmalllist())
    print(getList(10))
    print(getRandomList(10))
