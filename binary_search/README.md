# 📌 Binary Search

## 1. Basic Information

**Definition**: A fast search algorithm that finds the position of a target value within a sorted array by repeatedly dividing the search space in half.

**Physical Representation**: Works directly on sorted arrays or ranges of values.

**Key Analogy**: Looking for a word in a dictionary by opening the book in the middle, and determining if the word is in the left half or the right half.

**In Python:**  
- Typically implemented using a `while` loop with `left` and `right` pointers.
- Can also use the built-in `bisect` module.

**When to Use Binary Search:**  
- Finding an element in a sorted array.
- Finding boundaries or first/last occurrences.
- "Binary search on answer" for optimization problems.

---

## 2. Basic Operations

- **Search**: Finding if a target exists and returning its index.
- **Lower Bound**: Finding the first index where an element is >= target.
- **Upper Bound**: Finding the first index where an element is > target.

---

## 3. Complexity Stats
| Operation  | Time(Average) | Time(Worst-Case) | Space     |
| --------   | -------       | --------         | -------   |
| Search     | $O(\log n)$   | $O(\log n)$      | $O(1)$    |

---
## 4. Common Problems

#### Pattern A: Basic Search
- Example Problem: Binary Search (LeetCode 704)
- Strategy: standard left, right = 0, n-1. While left <= right.

#### Pattern B: Search Boundaries
- Example Problem: Find First and Last Position of Element in Sorted Array
- Strategy: Use two binary searches, one to find the first occurrence, another to find the last.
