# e_insertionSort.py

"""
Title: Insertion Sort
Author:
Date-created: 21-09-2022
"""

from myFunctions import *


def insertionSort(LIST):
    """
    splits the list into a sorted and unsorted half and then takes the lowest index of the unsorted section and places it in its relative position in the sorted section.
    :param LIST:
    :return:
    """
    for i in range(1, len(LIST)):
        IND_VALUE = LIST[i]  # Saving the value of the lowest index in unsorted
        SORTED_IND = i - 1  # Identify largest of sorted section

        while SORTED_IND >= 0 and IND_VALUE < LIST[SORTED_IND]:
            # While traversing tail-to-head in the sorted section
            LIST[SORTED_IND + 1] = LIST[SORTED_IND]
            SORTED_IND = SORTED_IND - 1
        LIST[SORTED_IND + 1] = IND_VALUE  # Places value in correct index


if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        print(NUMBERS[:10])
        START = getTime()
        insertionSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(END - START)
    print(getAverage(TIMES))
