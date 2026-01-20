# Lab 4: Quicksort

## 1. Introduction and Objectives

### Overview
Implement quicksort using divide and conquer. Understand how pivot selection affects performance and why average case is O(n log n).

### Learning Objectives
- Understand divide and conquer strategy
- Implement quicksort algorithm
- Analyze best, average, and worst case complexity
- Compare with selection sort

### Prerequisites
- Complete Labs 1-3
- Read Chapter 4 in "Grokking Algorithms" (pages 55-76)

---

## 2. Algorithm Background

### Divide and Conquer
1. **Divide**: Split problem into smaller subproblems
2. **Conquer**: Solve subproblems (often recursively)
3. **Combine**: Merge solutions

### Quicksort Strategy
1. Pick a pivot element
2. Partition: elements < pivot go left, > pivot go right
3. Recursively sort left and right partitions

### Time Complexity
- **Best/Average Case**: O(n log n)
- **Worst Case**: O(n²) - when pivot is always min or max

---

## 3. Project Structure

```
lab04_quicksort/
├── quicksort.py   # Quicksort implementation
├── main.py        # Main program
└── README.md      # Your lab report
```

---

## 4. Step-by-Step Implementation

### Step 1: Create `quicksort.py`

```python
"""
Lab 4: Quicksort Implementation
Demonstrates divide and conquer from Chapter 4.

From Chapter 4: Quicksort uses D&C (Divide and Conquer):
1. Pick a pivot
2. Partition array into: less than pivot, pivot, greater than pivot
3. Recursively sort the sub-arrays
"""
from typing import List, Dict, Callable
import random


# ============================================
# EXACT CODE FROM CHAPTER 4 (page 65)
# ============================================
def quicksort(array):
    """
    Quicksort from Chapter 4.
    
    From the book (page 65):
    def quicksort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return quicksort(less) + [pivot] + quicksort(greater)
    """
    if len(array) < 2:
        # Base case: arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # Recursive case
        pivot = array[0]
        # Sub-array of all elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # Sub-array of all elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# ============================================
# RECURSIVE SUM FROM CHAPTER 4 (D&C example)
# ============================================
def sum_recursive(arr):
    """
    Sum using D&C - from Chapter 4 exercises.
    
    Base case: empty array = 0
    Recursive case: first element + sum of rest
    """
    if len(arr) == 0:
        return 0
    return arr[0] + sum_recursive(arr[1:])


def count_recursive(arr):
    """Count items using D&C - from Chapter 4 exercises."""
    if len(arr) == 0:
        return 0
    return 1 + count_recursive(arr[1:])


def max_recursive(arr):
    """Find max using D&C - from Chapter 4 exercises."""
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_recursive(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


# ============================================
# Verbose version for visualization
# ============================================
def quicksort_verbose(arr: List[int], depth: int = 0) -> List[int]:
    """Quicksort with detailed output to show the process."""
    indent = "  " * depth
    print(f"{indent}quicksort({arr})")
    
    if len(arr) < 2:
        print(f"{indent}→ Base case, returning {arr}")
        return arr
    
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    
    print(f"{indent}→ Pivot: {pivot}")
    print(f"{indent}→ Less: {less}, Greater: {greater}")
    
    sorted_less = quicksort_verbose(less, depth + 1)
    sorted_greater = quicksort_verbose(greater, depth + 1)
    
    result = sorted_less + [pivot] + sorted_greater
    print(f"{indent}→ Combined: {result}")
    return result


def quicksort_random_pivot(arr: List[int]) -> List[int]:
    """
    Quicksort with random pivot - avoids worst case on sorted input.
    
    From Chapter 4: "If you always choose a random element as the pivot,
    quicksort will complete in O(n log n) time on average."
    """
    if len(arr) < 2:
        return arr
    
    # Random pivot instead of first element
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    
    # Remove pivot and partition
    rest = arr[:pivot_idx] + arr[pivot_idx + 1:]
    less = [i for i in rest if i <= pivot]
    greater = [i for i in rest if i > pivot]
    
    return quicksort_random_pivot(less) + [pivot] + quicksort_random_pivot(greater)
```

### Step 2: Create `main.py`

```python
"""
Lab 4: Main Program
Demonstrates quicksort and divide & conquer from Chapter 4.
"""
from quicksort import (
    quicksort, quicksort_verbose, quicksort_random_pivot,
    sum_recursive, count_recursive, max_recursive
)


def main():
    # =========================================
    # PART 1: D&C Exercises from Chapter 4
    # =========================================
    print("=" * 60)
    print("PART 1: DIVIDE & CONQUER EXERCISES (Chapter 4)")
    print("=" * 60)
    
    # Sum using recursion
    arr = [2, 4, 6]
    print(f"\nsum_recursive({arr}) = {sum_recursive(arr)}")
    
    # Count using recursion
    arr = [1, 2, 3, 4, 5]
    print(f"count_recursive({arr}) = {count_recursive(arr)}")
    
    # Max using recursion
    arr = [3, 7, 2, 9, 1]
    print(f"max_recursive({arr}) = {max_recursive(arr)}")
    
    # =========================================
    # PART 2: Quicksort Step by Step
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: QUICKSORT VISUALIZATION")
    print("=" * 60)
    
    test_array = [10, 5, 2, 3]
    print(f"\nSorting {test_array}:")
    print("-" * 40)
    result = quicksort_verbose(test_array)
    print(f"\nResult: {result}")
    
    # =========================================
    # PART 3: Simple Quicksort
    # =========================================
    print("\n" + "=" * 60)
    print("PART 3: QUICKSORT FROM CHAPTER 4")
    print("=" * 60)
    
    print(f"\nquicksort([10, 5, 2, 3]) = {quicksort([10, 5, 2, 3])}")
    print(f"quicksort([33, 15, 10]) = {quicksort([33, 15, 10])}")
    print(f"quicksort([]) = {quicksort([])}")
    print(f"quicksort([5]) = {quicksort([5])}")
    
    # =========================================
    # PART 4: Worst Case vs Average Case
    # =========================================
    print("\n" + "=" * 60)
    print("PART 4: WORST CASE VS AVERAGE CASE (Chapter 4)")
    print("=" * 60)
    print("""
    From Chapter 4 (pages 72-75):
    
    WORST CASE: O(n²)
    - Happens when pivot is always smallest or largest
    - Example: Already sorted array with first-element pivot
    - Call stack height: O(n)
    
    BEST/AVERAGE CASE: O(n log n)  
    - Happens when pivot splits array roughly in half
    - Random pivot helps achieve this
    - Call stack height: O(log n)
    
    Why O(n log n)?
    - Each level of the call stack does O(n) work
    - With good pivots, there are O(log n) levels
    - Total: O(n) × O(log n) = O(n log n)
    
    "If you always choose a random element as the pivot,
    quicksort will complete in O(n log n) time on average."
    """)
    
    # Demonstrate with sorted array
    sorted_arr = list(range(1, 11))
    print(f"Sorting already-sorted array: {sorted_arr}")
    print("(This is worst case for first-element pivot!)")
    print(f"Result: {quicksort(sorted_arr)}")


if __name__ == "__main__":
    main()
```

---

## 5. Lab Report Template

```markdown
# Lab 4: Quicksort

## Student Information
- **Name:** [Your Name]
- **Date:** [Date]

## Divide and Conquer (from Chapter 4)

### D&C Steps
1. **Figure out the base case** - simplest possible case
2. **Divide/decrease** - until it becomes the base case

### Quicksort D&C
1. **Base case:** Array of 0 or 1 elements (already sorted)
2. **Recursive case:** Pick pivot, partition, recursively sort

## Code from Chapter 4

```python
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
```

## Complexity Analysis

| Case | Time | When It Happens |
|------|------|-----------------|
| Best | O(n log n) | Pivot splits evenly |
| Average | O(n log n) | Random pivot |
| Worst | O(n²) | Pivot always min/max |

## Reflection Questions

1. What is the base case for quicksort?

2. Why does pivot selection affect performance?

3. Trace quicksort([3, 5, 2, 1, 4]) showing each partition.
```

---

## 6. Submission
Save files in `lab04_quicksort/`, complete README, commit and push.
