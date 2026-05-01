# 📚 Data Structures & Algorithms

A comprehensive collection of common data structures and algorithms implemented in Python, designed for interview preparation and learning.

## 🎯 Overview

This repository contains well-documented implementations of fundamental data structures with common problem-solving patterns. Each data structure includes:

- **Detailed documentation** explaining concepts, operations, and complexity
- **Pattern-based implementations** covering common interview questions
- **Working code examples** ready to run and test
- **Time and space complexity analysis** for each operation

## 📂 Structure

```
data_structures_and_algorithms/
├── arrays/              # Array manipulation patterns
├── binary_search/       # Binary search techniques
├── dynamic_programming/ # DP, memoization, tabulation
├── graphs/              # Graph traversals and paths
├── hash_tables/         # Hash map techniques
├── heaps/               # Heap and priority queue patterns
├── linked_lists/        # Linked list operations
├── queues/              # Queue and BFS patterns
├── sorting/             # Sorting algorithms
├── stacks/              # Stack-based algorithms
├── trees/               # Tree traversals and operations
└── tries/               # Prefix tree patterns
```

Each directory contains:
- `README.md` - Comprehensive documentation with patterns and strategies
- `<name>.py` - Python implementations with examples

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher

### Running Examples

Each Python file includes example usage at the bottom. To test any data structure:

```bash
# Clone or navigate to the repository
cd data_structures_and_algorithms

# Run any data structure examples
python3 arrays/arrays.py
python3 binary_search/binary_search.py
python3 dynamic_programming/dynamic_programming.py
python3 graphs/graphs.py
python3 hash_tables/hash_tables.py
python3 heaps/heaps.py
python3 linked_lists/linked_lists.py
python3 queues/queues.py
python3 sorting/sorting.py
python3 stacks/stacks.py
python3 trees/trees.py
python3 tries/tries.py
```

### Using in Your Code

Import any pattern directly:

```python
from arrays.arrays import two_sum_sorted, max_subarray_sum_k
from binary_search.binary_search import binary_search, find_first_occurrence
from dynamic_programming.dynamic_programming import climb_stairs, knapsack
from graphs.graphs import bfs_traversal, dfs_traversal
from hash_tables.hash_tables import two_sum, group_anagrams
from heaps.heaps import find_kth_largest, merge_k_sorted_lists
from linked_lists.linked_lists import reverse_list, has_cycle
from queues.queues import bfs_graph, level_order_traversal
from sorting.sorting import merge_sort, quick_sort
from stacks.stacks import is_valid_parentheses, next_greater_element
from trees.trees import inorder_traversal, max_depth
from tries.tries import Trie
```

## 📖 Data Structures

### 1. Arrays
**Key Patterns**: Two Pointers, Sliding Window, Prefix Sum, Hashing, In-place Modification

**Common Problems**:
- Two Sum
- Maximum Subarray Sum
- Remove Duplicates
- Move Zeroes

[View Documentation →](arrays/README.md)

---

### 2. Linked Lists
**Key Patterns**: Fast & Slow Pointers, Reversal, Merge, In-place Modification, Runner Technique

**Common Problems**:
- Detect Cycle
- Reverse Linked List
- Merge Two Sorted Lists
- Remove Nth Node from End

[View Documentation →](linked_lists/README.md)

---

### 3. Stacks
**Key Patterns**: Balanced Parentheses, Monotonic Stack, Expression Evaluation, Backtracking

**Common Problems**:
- Valid Parentheses
- Next Greater Element
- Evaluate RPN
- Min Stack

[View Documentation →](stacks/README.md)

---

### 4. Queues
**Key Patterns**: BFS Traversal, Level Order, Sliding Window Maximum, Circular Queue, Multi-source BFS

**Common Problems**:
- Level Order Traversal
- Shortest Path (Unweighted)
- Sliding Window Maximum
- Rotting Oranges

[View Documentation →](queues/README.md)

---

### 5. Hash Tables
**Key Patterns**: Frequency Counting, Two Sum, Sliding Window, Caching, Set Operations

**Common Problems**:
- Two Sum
- Group Anagrams
- Longest Substring Without Repeating Characters
- LRU Cache

[View Documentation →](hash_tables/README.md)

---

### 6. Trees
**Key Patterns**: DFS Traversals, BFS, Tree Construction, LCA, Path Problems, BST Operations

**Common Problems**:
- Inorder/Preorder/Postorder Traversal
- Maximum Depth
- Lowest Common Ancestor
- Path Sum

[View Documentation →](trees/README.md)

---

### 7. Heaps
**Key Patterns**: Top K Elements, Merge K Sorted, Two Heaps, Scheduling, Heap Construction

**Common Problems**:
- Kth Largest Element
- Merge K Sorted Lists
- Find Median from Data Stream
- Meeting Rooms II

[View Documentation →](heaps/README.md)

---

### 8. Graphs
**Key Patterns**: BFS, DFS, Topological Sort, Shortest Path

**Common Problems**:
- Number of Islands
- Course Schedule
- Clone Graph
- Word Ladder

[View Documentation →](graphs/README.md)

---

### 9. Binary Search
**Key Patterns**: Binary Search, Lower/Upper Bound, Search in Rotated Array

**Common Problems**:
- Binary Search
- First Bad Version
- Find Minimum in Rotated Sorted Array
- Search a 2D Matrix

[View Documentation →](binary_search/README.md)

---

### 10. Dynamic Programming
**Key Patterns**: Memoization, Tabulation, 0/1 Knapsack, Unbounded Knapsack

**Common Problems**:
- Climbing Stairs
- Coin Change
- Longest Increasing Subsequence
- Partition Equal Subset Sum

[View Documentation →](dynamic_programming/README.md)

---

### 11. Tries
**Key Patterns**: Prefix Tree Construction, Word Search II

**Common Problems**:
- Implement Trie (Prefix Tree)
- Design Add and Search Words Data Structure
- Word Search II

[View Documentation →](tries/README.md)

---

### 12. Sorting
**Key Patterns**: Merge Sort, Quick Sort, Intervals

**Common Problems**:
- Merge Intervals
- Kth Largest Element in an Array (Quickselect)
- Sort Colors

[View Documentation →](sorting/README.md)

## 🧪 Testing

All implementations include test cases in the `if __name__ == "__main__":` block. Run individual files to see examples in action:

```bash
# Example: Test array patterns
python3 arrays/arrays.py

# Output:
# True
# 9
# True
# [1, 3, 12, 0, 0]
```

## 📊 Complexity Reference

Quick reference for common operations:

| Data Structure | Access    | Search    | Insert    | Delete    | Space     |
|---------------|-----------|-----------|-----------|-----------|-----------|
| Array         | O(1)      | O(n)      | O(n)      | O(n)      | O(n)      |
| Linked List   | O(n)      | O(n)      | O(1)*     | O(1)*     | O(n)      |
| Stack         | O(n)      | O(n)      | O(1)      | O(1)      | O(n)      |
| Queue         | O(n)      | O(n)      | O(1)      | O(1)      | O(n)      |
| Hash Table    | N/A       | O(1)†     | O(1)†     | O(1)†     | O(n)      |
| Binary Tree   | O(n)      | O(n)      | O(n)      | O(n)      | O(n)      |
| BST (balanced)| O(log n)  | O(log n)  | O(log n)  | O(log n)  | O(n)      |
| Heap          | N/A       | O(n)      | O(log n)  | O(log n)  | O(n)      |

\* O(1) if you have the pointer; O(n) if you need to find it first  
† Average case; O(n) worst case with collisions

## 🎓 Learning Path

Recommended order for studying:

1. **Arrays & Strings** - Foundation for all data structures
2. **Binary Search** - Essential optimization technique
3. **Sorting** - Core algorithmic foundations
4. **Linked Lists** - Pointer manipulation basics
5. **Stacks & Queues** - LIFO and FIFO patterns
6. **Hash Tables** - Fast lookups and counting
7. **Trees & Tries** - Hierarchical data and recursion
8. **Heaps** - Priority queues and top K problems
9. **Graphs** - Complex relationships and traversals
10. **Dynamic Programming** - Advanced problem solving

## 💡 Tips for Interview Prep

1. **Understand the pattern** - Don't just memorize solutions
2. **Analyze complexity** - Always discuss time and space trade-offs
3. **Test edge cases** - Empty inputs, single elements, duplicates
4. **Communicate clearly** - Explain your thought process
5. **Practice regularly** - Consistency beats cramming

## 🤝 Contributing

Feel free to:
- Add more patterns and examples
- Improve documentation
- Fix bugs or optimize solutions
- Add test cases

## 📝 License

This project is open source and available for educational purposes and created with the help of AI and me (Berat)

## 🔗 Resources

- [LeetCode](https://leetcode.com/) - Practice problems
- [NeetCode](https://neetcode.io/) - Curated problem lists
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - Complexity reference

---

**Happy Coding!** 🚀
