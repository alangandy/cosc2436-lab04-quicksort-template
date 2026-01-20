#!/usr/bin/env python3
"""
Lab 04: Quicksort - Interactive Tutorial
=========================================

🎯 GOAL: Implement quicksort using Divide & Conquer in quicksort.py

📚 DIVIDE AND CONQUER (D&C):
----------------------------
1. DIVIDE: Break problem into smaller subproblems
2. CONQUER: Solve subproblems (often recursively)
3. COMBINE: Merge solutions

QUICKSORT ALGORITHM:
1. Pick a PIVOT element
2. PARTITION: elements < pivot go LEFT, elements > pivot go RIGHT
3. Recursively sort LEFT and RIGHT
4. Combine: sorted_left + [pivot] + sorted_right

HOW TO RUN:
-----------
    python main.py           # Run this tutorial
    python -m pytest tests/ -v   # Run the grading tests
"""

from quicksort import quicksort, sum_recursive, count_recursive, max_recursive


def print_header(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def demo_quicksort() -> None:
    """Demonstrate the quicksort function."""
    print_header("QUICKSORT")
    
    print("""
    QUICKSORT STEP BY STEP:
    
    quicksort([10, 5, 2, 3])
    
    Step 1: Pick pivot = 10 (first element)
            less = [5, 2, 3]  (elements < 10)
            greater = []       (elements > 10)
    
    Step 2: Recursively sort less = quicksort([5, 2, 3])
            pivot = 5
            less = [2, 3]
            greater = []
            
            Recursively sort [2, 3]:
            pivot = 2
            less = []
            greater = [3]
            Result: [] + [2] + [3] = [2, 3]
            
            Result: [] + [5] + [] = wait, we need [2,3] first!
            Actually: quicksort([2,3]) + [5] + [] = [2, 3, 5]
    
    Step 3: Combine: [2, 3, 5] + [10] + [] = [2, 3, 5, 10]
    
    PYTHON IMPLEMENTATION:
    
    def quicksort(array):
        if len(array) < 2:          # Base case
            return array
        
        pivot = array[0]            # Pick first element as pivot
        
        # List comprehension - like a compact for loop!
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)
    """)
    
    test_cases = [
        [10, 5, 2, 3],
        [3, 2, 1],
        [1, 2, 3],
        [5],
        [],
        [3, 6, 8, 10, 1, 2, 1],
    ]
    
    for arr in test_cases:
        print(f"quicksort({arr}):", end=" ")
        try:
            result = quicksort(arr)
            expected = sorted(arr)
            if result == expected:
                print(f"✅ {result}")
            elif result is None:
                print("❌ Returned None")
            else:
                print(f"❌ Got {result}, expected {expected}")
        except Exception as e:
            print(f"❌ Error: {e}")


def demo_dc_exercises() -> None:
    """Demonstrate D&C exercises from Chapter 4."""
    print_header("D&C EXERCISES (Chapter 4)")
    
    print("""
    These exercises help you practice the D&C pattern:
    
    PATTERN:
        Base case: simplest input (empty array, single element)
        Recursive case: solve for first element + rest of array
    """)
    
    # Sum
    print("\n--- sum_recursive ---")
    print("Sum all elements using D&C")
    test_sums = [([1, 2, 3, 4], 10), ([5], 5), ([], 0)]
    for arr, expected in test_sums:
        try:
            result = sum_recursive(arr)
            status = "✅" if result == expected else "❌"
            print(f"  sum_recursive({arr}) = {result} {status}")
        except Exception as e:
            print(f"  sum_recursive({arr}) ❌ Error: {e}")
    
    # Count
    print("\n--- count_recursive ---")
    print("Count elements using D&C")
    test_counts = [([1, 2, 3, 4, 5], 5), ([42], 1), ([], 0)]
    for arr, expected in test_counts:
        try:
            result = count_recursive(arr)
            status = "✅" if result == expected else "❌"
            print(f"  count_recursive({arr}) = {result} {status}")
        except Exception as e:
            print(f"  count_recursive({arr}) ❌ Error: {e}")
    
    # Max
    print("\n--- max_recursive ---")
    print("Find maximum using D&C")
    test_maxes = [([1, 5, 3, 9, 2], 9), ([42], 42), ([1, 1, 1], 1)]
    for arr, expected in test_maxes:
        try:
            result = max_recursive(arr)
            status = "✅" if result == expected else "❌"
            print(f"  max_recursive({arr}) = {result} {status}")
        except Exception as e:
            print(f"  max_recursive({arr}) ❌ Error: {e}")


def python_list_comprehension() -> None:
    """Explain list comprehensions."""
    print_header("PYTHON LIST COMPREHENSIONS")
    
    print("""
    List comprehensions are a Python superpower! They're compact for loops.
    
    C++/JAVA STYLE:
    ---------------
    vector<int> less;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] < pivot) {
            less.push_back(arr[i]);
        }
    }
    
    PYTHON LIST COMPREHENSION:
    --------------------------
    less = [x for x in arr if x < pivot]
    
    READ IT AS:
    "Create a list of x, for each x in arr, if x < pivot"
    
    MORE EXAMPLES:
    --------------
    # Square all numbers
    squares = [x**2 for x in [1, 2, 3, 4]]  # [1, 4, 9, 16]
    
    # Filter even numbers
    evens = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]  # [2, 4]
    
    # Transform strings
    upper = [s.upper() for s in ["hello", "world"]]  # ["HELLO", "WORLD"]
    """)
    
    # Live demo
    print("LIVE DEMO:")
    arr = [10, 5, 2, 3, 8, 1]
    pivot = 5
    print(f"  arr = {arr}")
    print(f"  pivot = {pivot}")
    print(f"  less = [x for x in arr if x < pivot]")
    print(f"       = {[x for x in arr if x < pivot]}")
    print(f"  greater = [x for x in arr if x > pivot]")
    print(f"          = {[x for x in arr if x > pivot]}")


def complexity_analysis() -> None:
    """Explain quicksort complexity."""
    print_header("TIME COMPLEXITY")
    
    print("""
    QUICKSORT COMPLEXITY:
    
    Best/Average Case: O(n log n)
    - Each level processes n elements
    - There are log n levels (we divide in half each time)
    
    Worst Case: O(n²)
    - Happens when pivot is always smallest or largest
    - Example: already sorted array with first element as pivot
    
    WHY QUICKSORT IS FAST:
    - Average case is O(n log n)
    - Very cache-friendly (works on contiguous memory)
    - In practice, often faster than merge sort
    
    COMPARISON:
    
    Algorithm        Best      Average    Worst      Space
    ---------------------------------------------------------
    Selection Sort   O(n²)     O(n²)      O(n²)      O(1)
    Quicksort        O(n log n) O(n log n) O(n²)     O(log n)
    Merge Sort       O(n log n) O(n log n) O(n log n) O(n)
    
    For 1000 elements:
    - Selection Sort: ~1,000,000 operations
    - Quicksort:      ~10,000 operations (100x faster!)
    """)


def main():
    """Main entry point."""
    print("\n" + "⚡" * 30)
    print("   LAB 04: QUICKSORT")
    print("   Divide and Conquer!")
    print("⚡" * 30)
    
    print("""
    📋 YOUR TASKS:
    1. Open quicksort.py
    2. Implement these functions:
       - quicksort()
       - sum_recursive()
       - count_recursive()
       - max_recursive()
    3. Run this file to test: python main.py
    4. Run pytest when ready: python -m pytest tests/ -v
    """)
    
    demo_quicksort()
    demo_dc_exercises()
    python_list_comprehension()
    complexity_analysis()
    
    print_header("NEXT STEPS")
    print("""
    When all tests pass, run: python -m pytest tests/ -v
    Then complete the Lab Report in README.md
    """)


if __name__ == "__main__":
    main()
