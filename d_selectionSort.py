# d_selectionSort.py

"""
Title: Selection Sort
Author: Beatrix Bicomong
Date-created: 08-09-2022
"""

from myFunctions import *


def selectionSort(LIST):
    """
    Compares the current index value with the rest of the set. It will find the
    lowest value in the set and place it in the lowest index of the unsorted part of the list.
    :param LIST: list (int)
    :return: None
    """
    for i in range(len(LIST) - 1):  # for each place in the list (except the last)
        MIN_IND = i  # assume the index w/ lowest value is i
        for j in range(i + 1, len(LIST)):  # for each place after i (includes the last)
            if LIST[j] < LIST[MIN_IND]:  # test if subsequent value is less than the current assumed minimum
                MIN_IND = j  # update the index of the current assumed min value
        if LIST[MIN_IND] < LIST[i]:  # test if minimum value is not at the start of the unsorted list
            # swaps the min value with the lowest index in the unsorted part of the list
            TEMP = LIST[i]
            LIST[i] = LIST[MIN_IND]
            LIST[MIN_IND] = TEMP

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        # print(NUMBERS[:10])
        START = getTime()
        selectionSort(NUMBERS)
        END = getTime()
        # print(NUMBERS[:10])
        print(END - START)
        TIMES.append(END - START)
    print(getAverage(TIMES))