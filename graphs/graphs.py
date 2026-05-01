"""
graphs.py

A collection of common graph patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

from collections import deque
from typing import List, Dict, Set

# ---------------------------------------------------------
# Pattern A: Breadth-First Search (BFS)
# ---------------------------------------------------------

def bfs_traversal(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    """
    Traverses a graph level by level.
    Time: O(V + E)
    Space: O(V)
    """
    visited = set([start_node])
    queue = deque([start_node])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return result

# ---------------------------------------------------------
# Pattern B: Depth-First Search (DFS)
# ---------------------------------------------------------

def dfs_traversal(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    """
    Traverses a graph by going as deep as possible.
    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    result = []
    
    def dfs(node: int):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        
        for neighbor in graph.get(node, []):
            dfs(neighbor)
            
    dfs(start_node)
    return result

# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------

if __name__ == "__main__":
    adj_list = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [5],
        5: []
    }
    
    print(bfs_traversal(adj_list, 1))  # [1, 2, 3, 4, 5]
    print(dfs_traversal(adj_list, 1))  # [1, 2, 4, 5, 3]
