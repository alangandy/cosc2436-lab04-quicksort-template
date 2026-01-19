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

---

## Complete Solutions

### Task 1: `quicksort()` - Complete Implementation

```python
def quicksort(array: List[int]) -> List[int]:
    """
    Sort array using quicksort.
    
    From Chapter 4 (page 65):
    Base case: arrays with 0 or 1 element are already sorted
    Recursive case: pick pivot, partition, recursively sort
    
    Time Complexity: O(n log n) average, O(n²) worst
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(array) < 2:
        return array
    
    # Pick the first element as the pivot
    pivot = array[0]
    
    # Partition: elements less than pivot go to 'less', greater go to 'greater'
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]
    
    # Recursively sort and combine
    return quicksort(less) + [pivot] + quicksort(greater)
```

**How it works:**
1. **Base case**: If array has 0 or 1 elements, it's already sorted - return it
2. **Choose pivot**: Use the first element `array[0]`
3. **Partition**: Use list comprehensions to split remaining elements:
   - `less`: all elements ≤ pivot (from `array[1:]`)
   - `greater`: all elements > pivot (from `array[1:]`)
4. **Combine**: Recursively sort both partitions and concatenate: `sorted_less + [pivot] + sorted_greater`

**Step-by-step example for `quicksort([10, 5, 2, 3])`:**
```
quicksort([10, 5, 2, 3])
  pivot = 10
  less = [5, 2, 3]  (all <= 10)
  greater = []      (none > 10)
  return quicksort([5, 2, 3]) + [10] + quicksort([])
  
  quicksort([5, 2, 3])
    pivot = 5
    less = [2, 3]   (all <= 5)
    greater = []    (none > 5)
    return quicksort([2, 3]) + [5] + []
    
    quicksort([2, 3])
      pivot = 2
      less = []     (none <= 2)
      greater = [3] (3 > 2)
      return [] + [2] + quicksort([3])
      
      quicksort([3]) → [3]  (base case)
      
      return [] + [2] + [3] = [2, 3]
    
    return [2, 3] + [5] + [] = [2, 3, 5]
  
  return [2, 3, 5] + [10] + [] = [2, 3, 5, 10]
```

---

### Task 2: `sum_recursive()` - Complete Implementation

```python
def sum_recursive(arr: List[int]) -> int:
    """
    Sum array using D&C (Chapter 4 exercise).
    
    Base case: empty array = 0
    Recursive case: first + sum(rest)
    """
    # Base case: empty array has sum of 0
    if len(arr) == 0:
        return 0
    
    # Recursive case: first element + sum of rest
    return arr[0] + sum_recursive(arr[1:])
```

---

### Task 3: `count_recursive()` - Complete Implementation

```python
def count_recursive(arr: List) -> int:
    """Count items using D&C."""
    # Base case: empty array has 0 items
    if len(arr) == 0:
        return 0
    
    # Recursive case: 1 + count of rest
    return 1 + count_recursive(arr[1:])
```

---

### Task 4: `max_recursive()` - Complete Implementation

```python
def max_recursive(arr: List[int]) -> int:
    """Find max using D&C."""
    # Base case: single element is the max
    if len(arr) == 1:
        return arr[0]
    
    # Base case: two elements - return larger
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    
    # Recursive case: max of first vs max of rest
    sub_max = max_recursive(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
```

---

## Example Usage

```python
# Quicksort
>>> quicksort([10, 5, 2, 3])
[2, 3, 5, 10]

>>> quicksort([3, 1, 4, 1, 5, 9, 2, 6])
[1, 1, 2, 3, 4, 5, 6, 9]

>>> quicksort([])
[]

>>> quicksort([42])
[42]

# Sum recursive
>>> sum_recursive([1, 2, 3, 4, 5])
15

# Count recursive
>>> count_recursive([1, 2, 3, 4, 5])
5

# Max recursive
>>> max_recursive([3, 7, 2, 9, 1])
9
```

---

## Testing
```bash
python -m pytest tests/ -v
```

## Submission
Commit and push your completed `quicksort.py` file.
