# 📌 Sorting Algorithms

## 1. Basic Information

**Definition**: Algorithms that put elements of a list into a certain order (usually numerical or lexicographical).

**Physical Representation**: Modifying an array in-place, or creating a new sorted array.

**Key Analogy**: Organizing a mixed deck of cards by suit and rank.

**In Python:**  
- Python uses Timsort (a hybrid of Merge Sort and Insertion Sort) for its built-in `sort()` and `sorted()`.
- However, interviews may ask you to implement classic algorithms from scratch.

**When to Use Sorting:**  
- As a preprocessing step (e.g., before binary search).
- To group similar items together.
- To find the k-th smallest/largest element (though Heap or Quickselect is often better).

---

## 2. Basic Algorithms

- **Merge Sort**: Divide array in half, sort halves, merge. Extremely stable.
- **Quick Sort**: Pick a pivot, partition around pivot, sort sides. Very fast in practice.
- **Bubble / Insertion / Selection Sort**: $O(n^2)$ basic sorts. Good to know for theory.

---

## 3. Complexity Stats
| Algorithm    | Time (Average) | Time (Worst) | Space |
| --------     | -------        | -------      | ----- |
| Merge Sort   | $O(n \log n)$  | $O(n \log n)$| $O(n)$|
| Quick Sort   | $O(n \log n)$  | $O(n^2)$     | $O(\log n)$ |
| Built-in Sort| $O(n \log n)$  | $O(n \log n)$| $O(n)$|

---
## 4. Common Problems

#### Pattern A: Merge Intervals
- Example Problem: Merge Overlapping Intervals
- Strategy: Sort by start time, then iterate and merge if `start <= previous_end`.

#### Pattern B: Quickselect
- Example Problem: Kth Largest Element in an Array
- Strategy: Use the Quick Sort partitioning logic to find the Kth element in $O(n)$ average time without fully sorting.
