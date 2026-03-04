# 📌 Queues

## 1. Basic Information

**Definition**: A queue is a First-In-First-Out (FIFO) data structure. The first element added is the first one removed. Like waiting in line at a coffee shop.

**Physical Representation**: Can be implemented using an array (circular buffer) or linked list. Elements are added at the back (enqueue) and removed from the front (dequeue).

**Key Analogy**: A line at Starbucks. First person in line gets served first. No cutting allowed.

**In Python:**  
- Implemented using `collections.deque` (double-ended queue)
- Can also use `queue.Queue` for thread-safe operations
- Dynamic size

**When to Use Queues:**  
- Task scheduling and job processing
- Breadth-First Search (BFS)
- Managing requests in order
- Buffering data streams
> When stuck, ask: “Is this a shortest-path problem or an exploration problem?” That alone solves 80% of confusion.

---

## 2. Basic Operations

- **Enqueue**: Add an element to the back of the queue.

- **Dequeue**: Remove and return the front element from the queue.

- **Peek/Front**: View the front element without removing it.

- **isEmpty**: Check if the queue is empty.

---

## 3. Complexity Stats
| Operation  | Time(Average) | Time(Worst-Case) | Space     |
| --------   | -------       | --------         | -------   |
| Enqueue    | $O(1)$      | $O(1)$         | $O(1)$  |
| Dequeue    | $O(1)$      | $O(1)$         | $O(1)$  |
| Peek       | $O(1)$      | $O(1)$         | $O(1)$ |
| Search     | $O(n)$      | $O(n)$         |$O(1)$|

---
## 4. Common Problems
This is how you know which tool to grab when you're staring at a problem and drawing a blank.

#### Pattern A: BFS Traversal
- Example Problem: Level Order Traversal, Shortest Path in Unweighted Graph
- Strategy:
    - Start from the root/source node
    - Add neighbors to the queue
    - Process nodes level by level
    - Mark visited nodes to avoid cycles

#### Pattern B: Sliding Window with Queue
- Example Problem: Sliding Window Maximum
- Strategy:
    - Use a deque to maintain elements in window
    - Keep elements in decreasing order
    - Remove elements outside the window from front
    - Remove smaller elements from back

#### Pattern C: Multi-level Processing
- Example Problem: Rotting Oranges, Walls and Gates
- Strategy:
    - Add all starting points to queue
    - Process all nodes at current level before moving to next
    - Track time/distance as you go
    - Use BFS to spread outward

#### Pattern D: Circular Queue
- Example Problem: Design Circular Queue, Moving Average
- Strategy:
    - Use fixed-size array with head and tail pointers
    - Wrap around using modulo operation
    - Track size to distinguish full vs empty
