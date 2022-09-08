"""
Title: Linear Search Example
Author: Beatrix Bicomong
Date-created: 02-09-2022
"""

import time, random, statistics

# Make a large data set
NUMBERS = []
for i in range(200000000):
    if random.randrange(2) == 1:
        NUMBERS.append(i)
TIMES = []

for i in range(30):
    # Search for a value in the data set
    NUMBER = NUMBERS[random.randrange(len(NUMBERS))]
    print(NUMBER)

    # Linear component of algorithm
    START_TIME = time.perf_counter()
    for i in range(len(NUMBERS)):
        if NUMBERS[i] == NUMBER:
            print("FOUND")
            break
    END_TIME = time.perf_counter()
    TOTAL_TIME = END_TIME - START_TIME
    TIMES.append(TOTAL_TIME)

# Calculate average search time
print(statistics.mean(TIMES))
