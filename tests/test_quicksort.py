"""Lab 04: Test Cases for Quicksort"""
import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from quicksort import quicksort, sum_recursive, count_recursive, max_recursive


class TestQuicksort:
    def test_basic(self):
        assert quicksort([10, 5, 2, 3]) == [2, 3, 5, 10]
    
    def test_empty(self):
        assert quicksort([]) == []
    
    def test_single(self):
        assert quicksort([5]) == [5]
    
    def test_sorted(self):
        assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    def test_reverse(self):
        assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    def test_duplicates(self):
        assert quicksort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


class TestDCExercises:
    def test_sum(self):
        assert sum_recursive([2, 4, 6]) == 12
        assert sum_recursive([]) == 0
    
    def test_count(self):
        assert count_recursive([1, 2, 3, 4, 5]) == 5
        assert count_recursive([]) == 0
    
    def test_max(self):
        assert max_recursive([3, 7, 2, 9, 1]) == 9


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
