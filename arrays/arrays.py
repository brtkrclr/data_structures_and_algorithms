"""
arrays.py

A collection of common array patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

from typing import List


# ---------------------------------------------------------
# Pattern A: Two Pointers
# ---------------------------------------------------------

def two_sum_sorted(nums: List[int], target: int) -> bool:
    """
    Given a sorted array, determine if two numbers sum to target.
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


def remove_duplicates(nums: List[int]) -> int:
    """
    Removes duplicates from a sorted array in-place.
    Returns the length of the unique portion.
    Time: O(n)
    Space: O(1)
    """
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k


# ---------------------------------------------------------
# Pattern B: Sliding Window
# ---------------------------------------------------------

def max_subarray_sum_k(nums: List[int], k: int) -> int:
    """
    Finds the maximum sum of any subarray of size k.
    Time: O(n)
    Space: O(1)
    """
    if len(nums) < k:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def longest_subarray_under_limit(nums: List[int], limit: int) -> int:
    """
    Finds the longest subarray with sum <= limit.
    Time: O(n)
    Space: O(1)
    """
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > limit:
            current_sum -= nums[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# ---------------------------------------------------------
# Pattern C: Prefix Sum
# ---------------------------------------------------------

def build_prefix_sum(nums: List[int]) -> List[int]:
    """
    Builds a prefix sum array.
    Time: O(n)
    Space: O(n)
    """
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    return prefix


def range_sum(prefix: List[int], left: int, right: int) -> int:
    """
    Returns sum of elements from index left to right (inclusive).
    Time: O(1)
    """
    return prefix[right + 1] - prefix[left]


# ---------------------------------------------------------
# Pattern D: Hashing with Arrays
# ---------------------------------------------------------

def contains_duplicate(nums: List[int]) -> bool:
    """
    Checks if the array contains any duplicates.
    Time: O(n)
    Space: O(n)
    """
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


def two_sum_unsorted(nums: List[int], target: int) -> List[int]:
    """
    Returns indices of two numbers that add up to target.
    Time: O(n)
    Space: O(n)
    """
    index_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in index_map:
            return [index_map[diff], i]
        index_map[num] = i

    return []


# ---------------------------------------------------------
# Pattern E: In-place Modification
# ---------------------------------------------------------

def move_zeroes(nums: List[int]) -> None:
    """
    Moves all zeroes to the end while maintaining order.
    Time: O(n)
    Space: O(1)
    """
    k = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1

    for i in range(k, len(nums)):
        nums[i] = 0


def remove_element(nums: List[int], val: int) -> int:
    """
    Removes all occurrences of val in-place.
    Returns the new length.
    Time: O(n)
    Space: O(1)
    """
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


# ---------------------------------------------------------
# Example Usage (for local testing)
# ---------------------------------------------------------

if __name__ == "__main__":
    print(two_sum_sorted([1, 2, 3, 4, 6], 6))          # True
    print(max_subarray_sum_k([2, 1, 5, 1, 3, 2], 3))   # 9
    print(contains_duplicate([1, 2, 3, 1]))           # True

    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print(nums)                                       # [1, 3, 12, 0, 0]
