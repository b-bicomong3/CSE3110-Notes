# CSE3110 Iterative Algorithms
## Iterative algorithms
Iterative algorithms are algorithms that use loops to process large sets of data this includes while loops and for loops. In contrast, Recursive Algorithms are algorithms that call the same algorithm over and over again to process large set of data. Iterative Algorithms tend to be easier to design, but increase in efficiency when using recursive algorithms.

Iterative algorithms are easily shown in search and sort algorithms.
### Linear Search
Linear search is the easiest to program, but least efficient method of search. It processes the data line by line, similar to brute force decryption algorithms when cracking passwords.

```python
FOUND = False
for i in range(len(LIST)):
    if VALUE == LIST[i]:
        FOUND = True
        break
```

Linear search processing time is dependent on the length of the array and the value's placement in the array. Arrays that are 10000 indices or higher can have a noticeable time requirement to process.

### Measuring processing time
we use ```time.perf_counter()``` to measure the overall time taken between processing data.

For more accurate results, we use the average of at least 3- trials and then use ```statistics.mean()``` to find the average.

