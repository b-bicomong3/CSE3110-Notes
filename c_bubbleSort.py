# c_bubbleSort.py
"""
Title: Bubble Sort
Author: Beatrix Bicomong
Date-created: 08-09-2022
"""
from myFunctions import *


def bubbleSort(LIST):
    """
    Compares two adjacent values and moves the highest one to the end of the list.
    :param LIST: list (int)
    :return: None
    """
    for i in range(len(LIST) - 1, 0, -1):  # traversed backwards from end to index 1
        for j in range(i):
            if LIST[j] > LIST[j + 1]:  # if left Num is greater than right Num
                # switch the two values
                TEMP = LIST[j]
                LIST[j] = LIST[j + 1]
                LIST[j + 1] = TEMP
                # LIST[j], LIST[j+1] = LIST[j+1], LIST[j]


if __name__ == "__main__":
    from random import shuffle

    TIMES = []
    NUMBERS = getList(1000000)
    for i in range(30):
        shuffle(NUMBERS)
        print(NUMBERS[:5])
        START = getTime()
        bubbleSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(TIMES[-1])
    print(getAverage(TIMES))
