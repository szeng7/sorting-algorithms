# sorting-algorithms

This is a Matplotlib visualization of various sorting algorithms.

## How to Run

```
python sorting.py <type-of-sorting>
```

## Notes

The current supported sorting algorithms are
- bubble sort
- insertion sort
- selection sort
- quick sort
- merge sort
- heap sort
- bucket sort (bucket size is 10)
- radix sort

with all of initialized arrays being [0, 2, 4 ... 198] randomized (basically all 100 values starting from 0 and going by increments of 2). By changing the value of N in the code, you'll
be able to start with larger arrays.

The number of operations count is relatively accurate for the first few sorts, such as bubble sort, insertion sort and selection sort. However, with some of the latter sorts, the
count is rather misleading due to it being attached to the number of times that the figure is updated. For example, with bucket sort, it's hard to, especially with it being in place, it's difficult to visualize, so the animation is more of a guideline for how the sort would work but the number of operations count isn't true to the actual number of operations. Future work may be done to disconnect the update count and the operations count for more accuracy.