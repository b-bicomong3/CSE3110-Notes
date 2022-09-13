# CSE3110 Iterative Algorithms

## Iterative algorithms

Iterative algorithms are algorithms that use loops to process large sets of data this includes while loops and for
loops. In contrast, Recursive Algorithms are algorithms that call the same algorithm over and over again to process
large set of data. Iterative Algorithms tend to be easier to design, but increase in efficiency when using recursive
algorithms.

Iterative algorithms are easily shown in search and sort algorithms.

### Linear Search

Linear search is the easiest to program, but least efficient method of search. It processes the data line by line,
similar to brute force decryption algorithms when cracking passwords.

```python
FOUND = False
for i in range(len(LIST)):
    if VALUE == LIST[i]:
        FOUND = True
        break
```

Linear search processing time is dependent on the length of the array and the value's placement in the array. Arrays
that are 10000 indices or higher can have a noticeable time requirement to process.

### Measuring processing time

we use ```time.perf_counter()``` to measure the overall time taken between processing data.

For more accurate results, we use the average of at least 3- trials and then use ```statistics.mean()``` to find the
average.

### Binary Search

Binary Search follows the _divide and conquer_ technique of finding a value. It takes an __ordered__ set of data and
tests the midpoint. Then it cuts the list in half and reruns the process.

**Steps for Binary Search**

1. Determine the Midpoint of the list.
2. Test if the Midpoint is the found value.
    1. If the Midpoint is the found value, end
    2. If the value is larger than the midpoint, redefine the lowest value of the list to be one above the midpoint.
    3. If the value is smaller than the midpoint, redefine the largest value of the list to be one below the midpoint.
3. Repeat until the value is found

* Advantages of Binary Search
    * It is significantly faster than linear search
* Disadvantages of Binary Search
    * List Must already be sorted from smallest to largest
    * List must only contain integers or floats
    * Harder to program

### Sorting Data

Just like searching algorithms, sorting algorithms have varying levels of efficiency. There are several types of sort
algorithms including bubble, selection, insertion, and merge. (Python uses Timsort, which is a hybrid od merge and
insertion sort designed by Time Peters in 2002)

### Bubble Sort

Bubble sort compares two adjacent values on the list and arranges them from lowest to highest. Then it moves to the next
index pair and repeats until it reaches the end of the unsorted list. The final index is the value that is sorted and
the algorithm repeats until each index (traversed tail-to-head) is sorted.
Advantages are that it is easy to program and takes less memory, but the disadvantages are that its processing time is
directly proportional to the length of the data set. However, the set is often fully sorted before the last iteration.

| 1 | 5 | 3 | 19 | 11 | 17     | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 5 | 11 | 17 | 7      | 13 | __19__ |
| 1 | 3 | 5 | 11 | 7 | 13     | __17__ | 19 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 17 | 19 |
| 1 | 3 | 5 | 7 | __11__ | 13     | 17 | 19 |
| 1 | 3 | 5 | __7__ | 11 | 13     | 17 | 19 |
| 1 | 3 | __5__ | 7 | 11 | 13     | 17 | 19 |
| 1 | __3__ | 5 | 7 | 11 | 13     | 17 | 19 |

### Selection Sort

Selection sort compares the current index value with the rest of the set. It will find the lowest value and switch
positions with the lowest index position of the unsorted half of the list. As it runs through the data set, it will
select the lowest values and place them in the lower positions on the list.

| 1       | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
|---------| --- | --- | --- | --- | --- | --- |---|
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1       | __3__ | _5_ | 19 | 11 | 17 | 7 | 13 |
| 1       | 3 | __*5*__ | 19 | 11 | 17 | 7 | 13 |
| 1       | 3 | 5 | __7__ | 11 | 17 | _19_ | 13 |
| 1       | 3 | 5 | 7 | __*11*__ | 17 | 7 | 13 |
| 1       | 3 | 5 | 19 | 11 | __13__ | 7 | _17_ |
| 1       | 3 | 5 | 7 | 11 | 13 | __17__ | _19_ |

### Insertion

Insertion sort splits the list into two sections; sorted and unsorted. As it progresses through the list, it takes the
value at the lowest index of the unsorted half of the list and places it in the correct relative location in the sorted
section og the list.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __*5*__ | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | _3_ | __5__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __*19*__ | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | _11_ | __19__ | 17 | 7 | 13 |
| 1 | 3 | 5 | 11 | _17_ | __19__ | 7 | 13 |
| 1 | 3 | 5 | _7_ | 11 | 17 | __19__ | 13 |
| 1 | 3 | 5 | 7 | 11 | _13_ | 17 | __19__ |

# CSE3310 - Recursive Algorithm Notes

A __recursive algorithm__ calls itself with smaller or simpler input values. Recursive algorithm have a _base case_,
which is the simplest input value. Then there are subprocesses that simplifies more complex input values and returns the
simplified values to the same function.

All iterative algorithms can ve written recursively and vice verse; however, certain functions are easier to write in
one form over the other.

### Example 1: Testing for correct input

```python
# iterative
def chckInt(x):
    while True:
        if x.isnumeric():
            return int(x)
        else:
            print("You did not enter a number.")
            x = input("Enter a number: ")


# recursive
def chckInt(x):
    if x.isnumeric():
        # base case
        return (x)
    else:
        print("You did not enter a number: ")
        return chckInt(input("Enter a number: "))  # updates x and returns it into the function
```

### Iteration vs. Recursion

In general, iterative algorithms require more lines of code and more variables. It relies on while and for loops to
complete the process. Whereas, recursive algorithms do not use as many variables or loops because return values are
re-entered into a new instance of the same function. Therefore, recursion requires more physical memory than iterative
algorithms because each instance of the recursive function stays in memory until the base case is achieved.

Iterative algorithms tend to be faster than exclusively recursive algorithms; however, hybrid algorithms that are use
both can be faster than exclusively iterative algorithms.

## Example 2: Factorials

### Calculate 7!

7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1

But...

6! = 6 * 5 * 4 * 3 * 2 * 1 * 1

Thus, we can rewrite 7! as,

7! = 7 * 6!

Going onwards,

7! = 7 * (6 * (5 * (4 * (3 * (2 * (1 * (1)))))))

Generalize Factorials as,

```
f(x) = x * (f(x-1)), x > 0
     = 1, x = 0 // base case
```

### Sorting 
Recursive sorting uses both recursive and iterative processes. In general these hybrid sorts are exponentially faster. (Measured in the logarithmic scale to be linear.)

Biology is the best class ever