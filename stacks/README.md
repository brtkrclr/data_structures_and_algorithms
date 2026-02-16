# 📌 Stacks

## 1. Basic Information

**Definition**: A stack is a Last-In-First-Out (LIFO) data structure. The last element added is the first one removed. Think of it like stacking plates—you can only take from the top.

**Physical Representation**: Can be implemented using an array or linked list. Elements are added and removed from one end (the "top").

**Key Analogy**: A stack of pancakes. You add new pancakes on top, and you eat from the top. You can't grab one from the middle without messing everything up.

**In Python:**  
- Implemented using `list` (with `append()` and `pop()`)
- Can also use `collections.deque` for better performance
- Dynamic size

**When to Use Stacks:**  
- Function call management (call stack)
- Undo/redo functionality
- Expression evaluation and syntax parsing
- Backtracking algorithms (DFS, maze solving)

---

## 2. Basic Operations

- **Push**: Add an element to the top of the stack.

- **Pop**: Remove and return the top element from the stack.

- **Peek/Top**: View the top element without removing it.

- **isEmpty**: Check if the stack is empty.

---

## 3. Complexity Stats
| Operation  | Time(Average) | Time(Worst-Case) | Space     |
| --------   | -------       | --------         | -------   |
| Push       | $O(1)$      | $O(1)$         | $O(1)$  |
| Pop        | $O(1)$      | $O(1)$         | $O(1)$  |
| Peek       | $O(1)$      | $O(1)$         | $O(1)$ |
| Search     | $O(n)$      | $O(n)$         |$O(1)$|

---
## 4. Common Problems
This is how you know which tool to grab when you're staring at a problem and drawing a blank.

#### Pattern A: Balanced Parentheses
- Example Problem: Valid Parentheses, Balanced Brackets
- Strategy:
    - Push opening brackets onto the stack
    - When you hit a closing bracket, pop and check if it matches
    - Stack should be empty at the end for valid input

#### Pattern B: Monotonic Stack
- Example Problem: Next Greater Element, Daily Temperatures
- Strategy:
    - Maintain elements in increasing or decreasing order
    - Pop elements that violate the monotonic property
    - Useful for finding next greater/smaller elements

#### Pattern C: Expression Evaluation
- Example Problem: Evaluate Reverse Polish Notation, Infix to Postfix
- Strategy:
    - Use stack to hold operands
    - Apply operators as you encounter them
    - Pop operands, compute, and push result back

#### Pattern D: Backtracking with Stack
- Example Problem: DFS Traversal, Path Finding
- Strategy:
    - Push current state onto stack
    - Explore one path fully before backtracking
    - Pop when you need to go back and try another path
