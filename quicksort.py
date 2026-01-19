"""
Lab 04: Quicksort
Implement quicksort using divide and conquer from Chapter 4.

D&C Strategy:
1. Pick a pivot
2. Partition: elements < pivot go left, > pivot go right
3. Recursively sort left and right
"""
from typing import List


def quicksort(array: List[int]) -> List[int]:
    """
    Sort array using quicksort.
    
    From Chapter 4 (page 65):
    Base case: arrays with 0 or 1 element are already sorted
    Recursive case: pick pivot, partition, recursively sort
    
    Time Complexity: O(n log n) average, O(n²) worst
    
    Example:
        >>> quicksort([10, 5, 2, 3])
        [2, 3, 5, 10]
    """
    # TODO: Implement quicksort
    # 1. Base case: if len(array) < 2, return array
    # 2. Pick pivot (first element)
    # 3. Partition into less and greater
    # 4. Return quicksort(less) + [pivot] + quicksort(greater)
    
    pass


def sum_recursive(arr: List[int]) -> int:
    """
    Sum array using D&C (Chapter 4 exercise).
    
    Base case: empty array = 0
    Recursive case: first + sum(rest)
    """
    # TODO: Implement
    pass


def count_recursive(arr: List) -> int:
    """Count items using D&C."""
    # TODO: Implement
    pass


def max_recursive(arr: List[int]) -> int:
    """Find max using D&C."""
    # TODO: Implement
    pass
