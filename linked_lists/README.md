# 📌 Linked Lists

## 1. Basic Information

**Definition**: A linked list is a collection of nodes where each node contains data and a pointer to the next node. Unlike arrays, nodes are scattered in memory and connected via pointers.

**Physical Representation**: Nodes are randomly scattered across memory. Each node holds a value and a reference (pointer) to the next node. The last node points to `None`.

**Key Analogy**: Think of a linked list like a scavenger hunt. Each clue (node) tells you where to find the next one. You can't skip ahead—you have to follow the trail.

**In Python:**  
- Implemented using custom `Node` class
- Dynamic size (grows/shrinks easily)
- No indexing—must traverse from head

**When to Use Linked Lists:**  
- Frequent insertions/deletions at the beginning
- Unknown or constantly changing size
- Don't need random access by index

---

## 2. Basic Operations

- **Access/Search**: No direct access—you gotta walk through from the head, checking each node one by one.

- **Insertion**: Super easy at the head (just rewire pointers). Inserting in the middle or end requires traversal first.

- **Deletion**: Remove a node by updating the previous node's pointer to skip over it. Easy once you find it.

- **Update**: Traverse to the node and change its value directly.

---

## 3. Complexity Stats
| Operation  | Time(Average) | Time(Worst-Case) | Space     |
| --------   | -------       | --------         | -------   |
| Access     | $O(n)$      | $O(n)$         | $O(1)$  |
| Search     | $O(n)$      | $O(n)$         | $O(1)$  |
| Insertion  | $O(1)$*      | $O(n)$         | $O(1)$ |
| Deletion   | $O(1)$*      | $O(n)$         |$O(1)$|

*O(1) if you already have the pointer to the node; O(n) if you need to find it first.

---
## 4. Common Problems
This is how you know which tool to grab when you're staring at a problem and drawing a blank.

#### Pattern A: Two Pointers (Fast & Slow)
- Example Problem: Detect Cycle, Find Middle Node
- Strategy:
    - Use two pointers moving at different speeds
    - Slow moves one step, fast moves two steps
    - If they meet, there's a cycle
    - When fast reaches the end, slow is at the middle

#### Pattern B: Reversal
- Example Problem: Reverse Linked List
- Strategy:
    - Keep track of previous, current, and next nodes
    - Flip the pointer direction one by one
    - Can be done iteratively or recursively

#### Pattern C: Merge & Combine
- Example Problem: Merge Two Sorted Lists
- Strategy:
    - Use a dummy node to simplify edge cases
    - Compare values and link the smaller one
    - Continue until one list is exhausted

#### Pattern D: In-place Modification
- Example Problem: Remove Nth Node from End
- Strategy:
    - Use two pointers with a gap of n nodes
    - Move both until the first reaches the end
    - The second pointer is now at the node to remove

#### Pattern E: Runner Technique
- Example Problem: Reorder List
- Strategy:
    - Find the middle using fast/slow pointers
    - Reverse the second half
    - Merge the two halves alternately
