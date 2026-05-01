"""
binary_search.py

A collection of common binary search patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

from typing import List

# ---------------------------------------------------------
# Pattern A: Basic Search
# ---------------------------------------------------------

def binary_search(nums: List[int], target: int) -> int:
    """
    Finds the target in a sorted array and returns its index.
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# ---------------------------------------------------------
# Pattern B: Find First Occurrence (Lower Bound)
# ---------------------------------------------------------

def find_first_occurrence(nums: List[int], target: int) -> int:
    """
    Finds the index of the first occurrence of a target.
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid
            right = mid - 1  # continue searching to the left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result

# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------

if __name__ == "__main__":
    arr = [1, 2, 4, 4, 4, 5, 6, 8]
    print(binary_search(arr, 5))             # 5
    print(binary_search(arr, 7))             # -1
    print(find_first_occurrence(arr, 4))     # 2
