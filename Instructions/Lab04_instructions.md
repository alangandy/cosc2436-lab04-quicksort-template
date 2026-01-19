# Lab 04: Quicksort

## Overview
In this lab, you will implement **Quicksort**, a fast divide-and-conquer sorting algorithm from Chapter 4 of "Grokking Algorithms."

## Learning Objectives
- Understand the divide and conquer (D&C) strategy
- Implement the quicksort algorithm
- Understand pivot selection and partitioning
- Compare O(n log n) average case vs O(n²) worst case

## Background

### Divide and Conquer Strategy
D&C algorithms work by:
1. **Divide**: Break the problem into smaller subproblems
2. **Conquer**: Solve the subproblems (often recursively)
3. **Combine**: Merge the solutions

### How Quicksort Works
1. Pick a **pivot** element
2. **Partition**: Elements smaller than pivot go left, larger go right
3. Recursively sort the left and right partitions
4. Combine: `sorted_left + [pivot] + sorted_right`

### Time Complexity
- **Average case**: O(n log n) - when pivot divides array roughly in half
- **Worst case**: O(n²) - when pivot is always the smallest/largest element

## Your Tasks

### Task 1: Implement `quicksort()`
Complete the `quicksort()` function in `quicksort.py`:
- Base case: arrays with 0 or 1 element are already sorted
- Pick the first element as pivot
- Partition into `less` (elements < pivot) and `greater` (elements > pivot)
- Return `quicksort(less) + [pivot] + quicksort(greater)`

### Task 2: Implement D&C Helper Functions
Also implement these D&C exercises:
- `sum_recursive()`: Sum array elements using D&C
- `count_recursive()`: Count array elements using D&C
- `max_recursive()`: Find maximum using D&C

## Example

```python
>>> quicksort([10, 5, 2, 3])
[2, 3, 5, 10]

# Step by step:
# pivot=10, less=[5,2,3], greater=[]
# quicksort([5,2,3]) + [10] + quicksort([])
#   pivot=5, less=[2,3], greater=[]
#   quicksort([2,3]) + [5] + []
#     pivot=2, less=[], greater=[3]
#     [] + [2] + [3] = [2,3]
#   [2,3] + [5] = [2,3,5]
# [2,3,5] + [10] = [2,3,5,10]
```

## Testing
```bash
python -m pytest tests/ -v
```

## Hints
- Use list comprehensions for partitioning:
  ```python
  less = [x for x in array[1:] if x <= pivot]
  greater = [x for x in array[1:] if x > pivot]
  ```
- Remember: `array[1:]` skips the first element (the pivot)
- The base case is crucial - don't forget it!

## Submission
Commit and push your completed `quicksort.py` file.
