# 📌 Hash Tables

## 1. Basic Information

**Definition**: A hash table (or hash map) is a data structure that maps keys to values using a hash function. It provides super fast lookups, insertions, and deletions on average.

**Physical Representation**: An array of "buckets" where each bucket can hold one or more key-value pairs. A hash function converts keys into array indices. Collisions are handled via chaining (linked lists) or open addressing.

**Key Analogy**: Think of a hash table like a library catalog. Instead of searching every book, you use the catalog (hash function) to jump straight to the shelf (bucket) where your book is.

**In Python:**  
- Implemented using `dict`
- Also available as `collections.defaultdict` and `collections.Counter`
- Dynamic resizing

**When to Use Hash Tables:**  
- Fast lookups by key
- Counting frequencies
- Detecting duplicates
- Caching/memoization

---

## 2. Basic Operations

- **Insert**: Add a key-value pair to the hash table.

- **Lookup/Get**: Retrieve the value associated with a key.

- **Delete**: Remove a key-value pair from the hash table.

- **Update**: Change the value associated with an existing key.

---

## 3. Complexity Stats
| Operation  | Time(Average) | Time(Worst-Case) | Space     |
| --------   | -------       | --------         | -------   |
| Insert     | $O(1)$      | $O(n)$         | $O(n)$  |
| Lookup     | $O(1)$      | $O(n)$         | $O(1)$  |
| Delete     | $O(1)$      | $O(n)$         | $O(1)$ |
| Update     | $O(1)$      | $O(n)$         |$O(1)$|

*Worst case happens with many hash collisions. Average case assumes good hash function.

---
## 4. Common Problems
This is how you know which tool to grab when you're staring at a problem and drawing a blank.

#### Pattern A: Frequency Counting
- Example Problem: Top K Frequent Elements, Group Anagrams
- Strategy:
    - Use a hash map to count occurrences
    - Iterate through the data once
    - Process the counts as needed (sort, filter, etc.)

#### Pattern B: Two Sum Pattern
- Example Problem: Two Sum, Four Sum, Subarray Sum Equals K
- Strategy:
    - Store complements or cumulative values in a hash map
    - Check if current element's complement exists
    - Track indices or counts as needed

#### Pattern C: Sliding Window with Hash Map
- Example Problem: Longest Substring Without Repeating Characters
- Strategy:
    - Use hash map to track last seen position of characters
    - Maintain a window with left and right pointers
    - Shrink window when duplicates are found

#### Pattern D: Group/Categorize
- Example Problem: Group Anagrams, Group Shifted Strings
- Strategy:
    - Create a unique key for each category
    - Use hash map where key = category, value = list of items
    - Iterate once and group items by their key
