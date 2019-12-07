# SORTING PARADIGM

## EXTERNAL SORTING
- sorts on data that can't be fit into memory
    - MergeSort is useful here
    
## Stable Sorting
- a sorting algorithm that maintains the original relative positioning of 
equivalent values.

- if OBJ A and OBJ B are equal, a stable algorithm ensures that 
    - if OBJ A comes before OBJ B before applying algorithm, 
        - it will come before it after applying the algorithm
        
        
## SORTING TABLE

| ALGORITHM | RUN TIME | TECHNIQUES | BEST USE CASES | 
| --- | --- | --- | --- |
| Insertion Sort | O(N^2) | Insertion | Very Small Arrays |
| Selection Sort | O(N^2) | Selection | Very Small Arrays | 
| Bubble Sort | O(N^2) | Two Way passes, restricting bounds of interest | Very small arrays, and mostly sorted arrays |
| Heap Sort | O (N log N) | Heaps, storing complete trees in an array | large arrays w/ unknown distribution |
| QuickSort | O (N log N), expected, O (N^2) worst case | Divide-and-Conquer, swapping items into position, randomization to avoid worst case behavior | large arrays without too many dupes, parallel sorting |
| MergeSort | O (N log N) | divide-and-conquer, merging, external sorting | large arrays w/ unknown distribution, huge amounts of data, parallel sorting |
| Counting Sort | O(N + M) | Counting | Large arrays of integers w/ a limited range of values |
| Bucket Sort | O(N + M) | Buckets | large arrays w/ reasonably uniform value distribution |
