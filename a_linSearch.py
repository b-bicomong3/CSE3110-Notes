"""
Title: Linear Search Example
Author: Beatrix Bicomong
Date-created: 02-09-2022
"""

import time, random, statistics

def recurLinSearch(LIST, VALUE):
    """
    search Linearly through the list to end a value
    :param LIST: list (int)
    :param VALUE: int
    :return: bool
    """
    if len(LIST) > 0:
        if LIST[0] == VALUE:
            return True
        else:
            return recurLinSearch(LIST[1:], VALUE)
    else:
        return False

# Make a large data set
NUMBERS = []
for i in range(20):
    if random.randrange(2) == 1:
        NUMBERS.append(i)
TIMES = []

for i in range(30):
    # Search for a value in the data set
    NUMBER = NUMBERS[random.randrange(len(NUMBERS))]
    print(NUMBER)

    START_TIME = time.perf_counter()
    '''
    # Linear component of algorithm
    for i in range(len(NUMBERS)):
        if NUMBERS[i] == NUMBER:
            print("FOUND")
            break
    '''
    print(recurLinSearch(NUMBERS, NUMBER))
    END_TIME = time.perf_counter()
    TOTAL_TIME = END_TIME - START_TIME
    TIMES.append(TOTAL_TIME)

# Calculate average search time
print(statistics.mean(TIMES))
