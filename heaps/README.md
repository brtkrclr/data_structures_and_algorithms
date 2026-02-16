# 📌 Heaps

## 1. Basic Information

**Definition**: A heap is a specialized tree-based data structure that satisfies the heap property. In a max heap, parent nodes are always greater than or equal to their children. In a min heap, parent nodes are always less than or equal to their children.

**Physical Representation**: Usually implemented as an array where for element at index `i`, left child is at `2i + 1`, right child is at `2i + 2`, and parent is at `(i - 1) // 2`.

**Key Analogy**: Think of a max heap like a corporate hierarchy where everyone is less important than their boss. The CEO is at the top, and importance decreases as you go down.

**In Python:**  
- Implemented using `heapq` module (min heap by default)
- For max heap, negate values or use custom comparator
- Efficient priority queue implementation

**When to Use Heaps:**  
- Finding min/max element quickly
- Priority queue implementations
- Top K problems
- Median finding in a stream

---

## 2. Basic Operations

- **Insert**: Add an element and bubble it up to maintain heap property.

- **Extract Min/Max**: Remove and return the root element, then heapify down.

- **Peek**: View the min/max element without removing it.

- **Heapify**: Convert an arbitrary array into a heap.

---

## 3. Complexity Stats
| Operation  | Time(Average) | Time(Worst-Case) | Space     |
| --------   | -------       | --------         | -------   |
| Insert     | $O(log n)$  | $O(log n)$     | $O(1)$  |
| Extract    | $O(log n)$  | $O(log n)$     | $O(1)$  |
| Peek       | $O(1)$      | $O(1)$         | $O(1)$ |
| Heapify    | $O(n)$      | $O(n)$         |$O(1)$|

---
## 4. Common Problems
This is how you know which tool to grab when you're staring at a problem and drawing a blank.

#### Pattern A: Top K Elements
- Example Problem: Kth Largest Element, Top K Frequent Elements
- Strategy:
    - Use a min heap of size K for Kth largest
    - Push elements and maintain heap size
    - The root is your answer
    - Time: O(n log k)

#### Pattern B: Merge K Sorted Lists/Arrays
- Example Problem: Merge K Sorted Lists
- Strategy:
    - Push the first element from each list into a min heap
    - Pop the smallest, add to result
    - Push the next element from that list
    - Repeat until heap is empty

#### Pattern C: Two Heaps (Median Finding)
- Example Problem: Find Median from Data Stream
- Strategy:
    - Use a max heap for smaller half
    - Use a min heap for larger half
    - Balance the heaps to keep sizes equal (or differ by 1)
    - Median is at the root(s)

#### Pattern D: Scheduling/Intervals
- Example Problem: Meeting Rooms II, Task Scheduler
- Strategy:
    - Use heap to track end times or availability
    - Sort events by start time
    - Use heap to manage overlapping intervals
