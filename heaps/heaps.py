"""
heaps.py

A collection of common heap patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

import heapq
from typing import List, Optional


# ---------------------------------------------------------
# Pattern A: Top K Elements
# ---------------------------------------------------------

def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Finds the kth largest element in an array.
    Time: O(n log k)
    Space: O(k)
    """
    # Use a min heap of size k
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return min_heap[0]


def top_k_frequent_elements(nums: List[int], k: int) -> List[int]:
    """
    Returns the k most frequent elements.
    Time: O(n log k)
    Space: O(n)
    """
    from collections import Counter
    
    count = Counter(nums)
    
    # Use a min heap of size k with (frequency, num) tuples
    min_heap = []
    
    for num, freq in count.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return [num for freq, num in min_heap]


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Finds k closest points to the origin.
    Time: O(n log k)
    Space: O(k)
    """
    # Use a max heap (negate distances) of size k
    max_heap = []
    
    for x, y in points:
        dist = -(x*x + y*y)  # Negate for max heap
        
        if len(max_heap) < k:
            heapq.heappush(max_heap, (dist, x, y))
        elif dist > max_heap[0][0]:
            heapq.heapreplace(max_heap, (dist, x, y))
    
    return [[x, y] for _, x, y in max_heap]


# ---------------------------------------------------------
# Pattern B: Merge K Sorted Lists/Arrays
# ---------------------------------------------------------

class ListNode:
    """Linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists.
    Time: O(n log k) where n is total number of nodes
    Space: O(k)
    """
    min_heap = []
    
    # Add first node from each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
    
    dummy = ListNode(0)
    current = dummy
    
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
    
    return dummy.next


def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """
    Merges k sorted arrays.
    Time: O(n log k)
    Space: O(k)
    """
    min_heap = []
    result = []
    
    # Add first element from each array with (value, array_idx, element_idx)
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
    
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Add next element from the same array
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))
    
    return result


# ---------------------------------------------------------
# Pattern C: Two Heaps (Median Finding)
# ---------------------------------------------------------

class MedianFinder:
    """
    Finds median from a data stream.
    """
    
    def __init__(self):
        self.small = []  # Max heap (negate values)
        self.large = []  # Min heap
    
    def add_num(self, num: int) -> None:
        """
        Adds a number to the data structure.
        Time: O(log n)
        """
        # Add to max heap (small)
        heapq.heappush(self.small, -num)
        
        # Balance: move largest from small to large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def find_median(self) -> float:
        """
        Returns the median.
        Time: O(1)
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        return (-self.small[0] + self.large[0]) / 2.0


# ---------------------------------------------------------
# Pattern D: Scheduling/Intervals
# ---------------------------------------------------------

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Finds minimum number of meeting rooms required.
    Time: O(n log n)
    Space: O(n)
    """
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min heap to track end times
    min_heap = []
    
    for start, end in intervals:
        # If earliest meeting has ended, reuse the room
        if min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
        
        heapq.heappush(min_heap, end)
    
    return len(min_heap)


def task_scheduler(tasks: List[str], n: int) -> int:
    """
    Finds minimum time to complete all tasks with cooling period.
    Time: O(n log 26) = O(n)
    Space: O(1) - at most 26 tasks
    """
    from collections import Counter
    
    task_counts = Counter(tasks)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)
    
    time = 0
    
    while max_heap:
        temp = []
        
        for _ in range(n + 1):
            if max_heap:
                count = heapq.heappop(max_heap)
                if count < -1:
                    temp.append(count + 1)
            
            time += 1
            
            if not max_heap and not temp:
                break
        
        for count in temp:
            heapq.heappush(max_heap, count)
    
    return time


# ---------------------------------------------------------
# Pattern E: Heap Construction
# ---------------------------------------------------------

def heapify_array(nums: List[int]) -> None:
    """
    Converts an array into a min heap in-place.
    Time: O(n)
    Space: O(1)
    """
    heapq.heapify(nums)


def kth_smallest_in_sorted_matrix(matrix: List[List[int]], k: int) -> int:
    """
    Finds kth smallest element in a sorted matrix.
    Time: O(k log n) where n is number of rows
    Space: O(n)
    """
    n = len(matrix)
    min_heap = []
    
    # Add first element from each row
    for r in range(min(n, k)):
        heapq.heappush(min_heap, (matrix[r][0], r, 0))
    
    result = 0
    
    for _ in range(k):
        result, r, c = heapq.heappop(min_heap)
        
        if c + 1 < len(matrix[r]):
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
    
    return result


# ---------------------------------------------------------
# Example Usage (for local testing)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Test kth largest
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
    
    # Test top k frequent
    print(top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    
    # Test merge k sorted arrays
    arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(merge_k_sorted_arrays(arrays))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Test median finder
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    print(mf.find_median())  # 1.5
    mf.add_num(3)
    print(mf.find_median())  # 2.0
    
    # Test meeting rooms
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(min_meeting_rooms(intervals))  # 2
    
    # Test k closest points
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    print(k_closest_points(points, 2))  # [[0, 1], [-2, 2]] or [[-2, 2], [1, 3]]
