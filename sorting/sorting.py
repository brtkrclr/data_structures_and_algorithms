"""
sorting.py

A collection of common sorting patterns and algorithms used in interviews,
implemented as small, focused functions.
"""

from typing import List

# ---------------------------------------------------------
# Pattern A: Merge Sort
# ---------------------------------------------------------

def merge_sort(nums: List[int]) -> List[int]:
    """
    Sorts an array using Merge Sort.
    Time: O(n log n)
    Space: O(n)
    """
    if len(nums) <= 1:
        return nums
        
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ---------------------------------------------------------
# Pattern B: Quick Sort
# ---------------------------------------------------------

def quick_sort(nums: List[int]) -> List[int]:
    """
    Sorts an array using Quick Sort.
    Time: O(n log n) average, O(n^2) worst
    Space: O(log n)
    """
    if len(nums) <= 1:
        return nums
        
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------

if __name__ == "__main__":
    arr1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(merge_sort(arr1))  # [1, 1, 2, 3, 4, 5, 5, 6, 9]
    
    arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(quick_sort(arr2))  # [1, 1, 2, 3, 4, 5, 5, 6, 9]
