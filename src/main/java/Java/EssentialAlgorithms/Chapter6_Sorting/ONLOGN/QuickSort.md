# QuickSort

Quick sort subdivides an array into two pieces, and then recursively calls itself to 
sort those pieces. 

## DIVIDER/MARKER

Picking the dividing item can be challenging. 
- The simplest method is to just pick the first item. 

PROBLEM
- However, if the item is sorted or sorted in reverse, the result is the worst case

METHODS FOR REMEDIATION: 

- one solution to avoid this is to randomize the array before calling quicksort, 
decreasing the likelihood that a bad divider will be selected
    - NOTE: for large arrays this is slow, so most devs don't do this. 
    
- another solution is to pick the middle of the first and last items making it 
unlikely that the marker is bad. 

- (MY FAVORITE)
    - just pick a random index from the part of the array being sorted. 
        
## PERFORMANCE
- QuickSort is "technically" not as fast as HeapSort, but it often runs faster.
- QuickSort tends not to handle duplication of values well. 

## PARALLELIZATION
- Quicksort is more flexible than Mergesort here, because while both can be 
parallelized, quicksort splits and merges based on size of structure. This means
we don't care about waiting for subsequent recursions.

