"""
queues.py

A collection of common queue patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

from collections import deque
from typing import List, Optional


# ---------------------------------------------------------
# Pattern A: BFS Traversal
# ---------------------------------------------------------

def bfs_graph(graph: dict, start: int) -> List[int]:
    """
    Performs BFS traversal on a graph.
    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result


def shortest_path_unweighted(graph: dict, start: int, end: int) -> int:
    """
    Finds shortest path length in an unweighted graph using BFS.
    Time: O(V + E)
    Space: O(V)
    """
    if start == end:
        return 0
    
    visited = {start}
    queue = deque([(start, 0)])
    
    while queue:
        node, distance = queue.popleft()
        
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return distance + 1
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1  # No path found


# ---------------------------------------------------------
# Pattern B: Level Order Traversal
# ---------------------------------------------------------

class TreeNode:
    """Binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Returns level-order traversal of a binary tree.
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Returns zigzag level-order traversal of a binary tree.
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(list(current_level))
        left_to_right = not left_to_right
    
    return result


# ---------------------------------------------------------
# Pattern C: Sliding Window Maximum
# ---------------------------------------------------------

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Finds the maximum in each sliding window of size k.
    Time: O(n)
    Space: O(k)
    """
    if not nums or k == 0:
        return []
    
    result = []
    dq = deque()  # Stores indices
    
    for i in range(len(nums)):
        # Remove elements outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result once we have a full window
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


# ---------------------------------------------------------
# Pattern D: Circular Queue
# ---------------------------------------------------------

class CircularQueue:
    """
    Implementation of a circular queue with fixed size.
    """
    
    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.tail = -1
        self.size = 0
        self.capacity = k
    
    def enqueue(self, value: int) -> bool:
        """Add element to the queue."""
        if self.is_full():
            return False
        
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True
    
    def dequeue(self) -> bool:
        """Remove element from the queue."""
        if self.is_empty():
            return False
        
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True
    
    def front(self) -> int:
        """Get the front element."""
        return -1 if self.is_empty() else self.queue[self.head]
    
    def rear(self) -> int:
        """Get the rear element."""
        return -1 if self.is_empty() else self.queue[self.tail]
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def is_full(self) -> bool:
        return self.size == self.capacity


# ---------------------------------------------------------
# Pattern E: Multi-source BFS
# ---------------------------------------------------------

def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Finds minimum time for all oranges to rot.
    Time: O(m * n)
    Space: O(m * n)
    """
    if not grid:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # Find all rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_count += 1
    
    if fresh_count == 0:
        return 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_time = 0
    
    while queue:
        r, c, time = queue.popleft()
        max_time = max(max_time, time)
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_count -= 1
                queue.append((nr, nc, time + 1))
    
    return max_time if fresh_count == 0 else -1


# ---------------------------------------------------------
# Example Usage (for local testing)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Test BFS
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    print(bfs_graph(graph, 2))  # [2, 0, 3, 1]
    
    # Test shortest path
    print(shortest_path_unweighted(graph, 0, 3))  # 2
    
    # Test sliding window maximum
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
    
    # Test circular queue
    cq = CircularQueue(3)
    print(cq.enqueue(1))  # True
    print(cq.enqueue(2))  # True
    print(cq.enqueue(3))  # True
    print(cq.enqueue(4))  # False (full)
    print(cq.front())     # 1
    print(cq.dequeue())   # True
    print(cq.enqueue(4))  # True
    print(cq.rear())      # 4
