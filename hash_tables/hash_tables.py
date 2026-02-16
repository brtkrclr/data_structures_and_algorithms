"""
hash_tables.py

A collection of common hash table patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

from typing import List, Dict
from collections import defaultdict, Counter


# ---------------------------------------------------------
# Pattern A: Frequency Counting
# ---------------------------------------------------------

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Returns the k most frequent elements.
    Time: O(n log k)
    Space: O(n)
    """
    count = Counter(nums)
    return [num for num, _ in count.most_common(k)]


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams together.
    Time: O(n * k log k) where k is max length of a string
    Space: O(n * k)
    """
    anagram_map = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        anagram_map[key].append(s)
    
    return list(anagram_map.values())


def first_unique_char(s: str) -> int:
    """
    Finds the first non-repeating character in a string.
    Time: O(n)
    Space: O(1) - at most 26 characters
    """
    count = Counter(s)
    
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    
    return -1


# ---------------------------------------------------------
# Pattern B: Two Sum Pattern
# ---------------------------------------------------------

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers that add up to target.
    Time: O(n)
    Space: O(n)
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    Counts number of subarrays with sum equal to k.
    Time: O(n)
    Space: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count


def four_sum_count(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    """
    Counts tuples (i,j,k,l) where A[i]+B[j]+C[k]+D[l] = 0.
    Time: O(n^2)
    Space: O(n^2)
    """
    sum_map = defaultdict(int)
    
    # Store all possible sums of A and B
    for a in A:
        for b in B:
            sum_map[a + b] += 1
    
    count = 0
    
    # Check if -(c + d) exists in sum_map
    for c in C:
        for d in D:
            count += sum_map[-(c + d)]
    
    return count


# ---------------------------------------------------------
# Pattern C: Sliding Window with Hash Map
# ---------------------------------------------------------

def length_of_longest_substring(s: str) -> int:
    """
    Finds length of longest substring without repeating characters.
    Time: O(n)
    Space: O(min(n, m)) where m is charset size
    """
    char_index = {}
    max_length = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


def min_window_substring(s: str, t: str) -> str:
    """
    Finds minimum window in s that contains all characters of t.
    Time: O(n + m)
    Space: O(m)
    """
    if not s or not t:
        return ""
    
    target_count = Counter(t)
    required = len(target_count)
    formed = 0
    
    window_counts = {}
    left = 0
    min_len = float('inf')
    min_left = 0
    
    for right, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in target_count and window_counts[char] == target_count[char]:
            formed += 1
        
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left
            
            char = s[left]
            window_counts[char] -= 1
            if char in target_count and window_counts[char] < target_count[char]:
                formed -= 1
            
            left += 1
    
    return "" if min_len == float('inf') else s[min_left:min_left + min_len]


# ---------------------------------------------------------
# Pattern D: Hash Map as Cache/Memo
# ---------------------------------------------------------

def fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:
    """
    Computes fibonacci number using memoization.
    Time: O(n)
    Space: O(n)
    """
    if memo is None:
        memo = {}
    
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


class LRUCache:
    """
    Least Recently Used cache with O(1) get and put.
    """
    
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.order = []
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move to end (most recently used)
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used
            lru = self.order.pop(0)
            del self.cache[lru]
        
        self.cache[key] = value
        self.order.append(key)


# ---------------------------------------------------------
# Pattern E: Set Operations
# ---------------------------------------------------------

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Finds intersection of two arrays.
    Time: O(n + m)
    Space: O(min(n, m))
    """
    return list(set(nums1) & set(nums2))


def is_isomorphic(s: str, t: str) -> bool:
    """
    Checks if two strings are isomorphic.
    Time: O(n)
    Space: O(1) - at most 256 characters
    """
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True


# ---------------------------------------------------------
# Example Usage (for local testing)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Test top k frequent
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    
    # Test group anagrams
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    
    # Test two sum
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    
    # Test longest substring
    print(length_of_longest_substring("abcabcbb"))  # 3
    
    # Test LRU cache
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))    # 1
    cache.put(3, 3)        # Evicts key 2
    print(cache.get(2))    # -1 (not found)
    
    # Test isomorphic
    print(is_isomorphic("egg", "add"))  # True
    print(is_isomorphic("foo", "bar"))  # False
