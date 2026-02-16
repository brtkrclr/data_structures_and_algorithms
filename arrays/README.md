# 📌 Arrays 

## 1. Basic Information

**Definition**: An array is a collection of elements stored in a fixed order, where each element can be accessed directly using an index. Fast, simple, and everywhere in coding interviews.

**Physical Representation**: All elements live next to each other in memory. One continuous chunk of RAM. If it needs to grow and there’s no space, the whole thing gets copied somewhere else.

**Key Analogy**: Think of an array like numbered lockers in a hallway. You can instantly open locker #7, but if you want to add one in the middle, everyone has to shift over.

**In Python:**  
- Implemented using `list`
- Dynamic size
- Zero-based indexing

**When to Use Arrays:**  
- Fast indexed access
- Fixed or predictable data structure
- Sequential data processing

---

## 2. Basic Operations

- **Access/Search**: Jump straight to an index in O(1), but searching an unsorted array means checking everything one by one.

- **Insertion**: Easy at the end, painful in the middle (everything shifts to make room).

- **Deletion**: Removing the last element is cheap; deleting from the front or middle makes everything slide left.

- **Update**: Directly overwrite a value at an index—fast and clean.

---

## 3. Complexity Stats
| Operation  | Time(Average) | Time(Worst-Case) | Space     |
| --------   | -------       | --------         | -------   |
| Access     | $O(1)$      | $O(1)$         | $O(1)$  |
| Search     | $O(n)$      | $O(n)$         | $O(1)$  |
| Insertion  | $O(n)$      | $O(n)$         | $O(1)$ |
| Deletion   | $O(n)$      | $O(n)$         |$O(1)$|

---
## 4. Common Prbolems
This is how you know which tool to grab when you're staring at a problem and drawing a blank.
#### Pattern A: Two Pointers
- Example Problem: Two Sum(sorted array), Remove duplicates
- Strategy: 
    - Start pointers at both ends (left and right)
    - Move inward based on condition
    - Works best when the array is sorted or when doing in-place edits
#### Pattern B: Sliding Window
- Example Problem: Maximum Subarray Sum of Size K
- Strategy:
    - Maintain a window of elements
    - Expand with the right pointer
    - Shrink from the left when constraints break
    - Perfect for contiguous subarray problems
#### Pattern C: Prefix Sum
- Example Problem: Subarray Sum Equals K
- Strategy:
    - Precompute cumulative sums
    - Convert range-sum problems into O(1) lookups
    - Often paired with hash maps
