# BubbleSort
Since there are two examples for BubbleSort, I'm putting the info about it in a separate file

## Basic Example
If an array is unsorted, then there must be two adjacent elements that are out of order. 

- The basic example is that bubble sort iterates repeatedly on (0, array.length) swapping
"out-of-order adjacencies" until there are no more out of order pairs remaining. 

## IMPROVEMENTS

### Alternating Iterations
Some elements aren't anywhere near their final position. i.e. they will require many swaps
to reach their final position in the array. 

- Iterations from Start to Finish speed up re-positioning of elements that are too low
- Iterations from Finish to Start speed up re-positioning of elements that are too high

- By alternating iterations (zig-zag) from 0 -> length -> 0 etc. we optimize for both.

### Multi-Swap
Another phenomenon related to the previous case is that some values might be able to be
swapped multiple times in a row. 
- by storing the element of interest for each iteration, we can compare it to multiple
successive values until we reach a point it can't be swapped. 
    - we can shift all of the elements we passed down or up (depending on our 
    direction) and insert the value. 
        - this does the work of multiple iterations in one.
        
### Decreasing Bounds
Lastly, as iterations progress, the edges of the array will become sorted. If the start
or finish of the array are sorted, we don't need to keep evaluating them. 
- If we track the last item in either direction, we can manage the "bounds" of the 
unsorted portion of the array. 
    - By shortening the traversal of each iteration, we increase the performance of the
    algorithm