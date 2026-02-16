# 📌 Trees

## 1. Basic Information

**Definition**: A tree is a hierarchical data structure with a root node and child nodes forming a parent-child relationship. Each node can have zero or more children, and there are no cycles.

**Physical Representation**: Nodes scattered in memory, each containing data and pointers to its children. Binary trees have at most two children per node (left and right).

**Key Analogy**: Think of a family tree or an org chart. One person at the top (root), and everyone else branches out below. No one reports to multiple people, and no circular reporting.

**In Python:**  
- Implemented using custom `TreeNode` class
- Each node has value and pointers to children
- Binary trees are most common in interviews

**When to Use Trees:**  
- Hierarchical data (file systems, org charts)
- Fast search, insert, delete (BST)
- Expression parsing
- Decision-making processes

---

## 2. Basic Operations

- **Traversal**: Visit all nodes in a specific order (in-order, pre-order, post-order, level-order).

- **Search**: Find a node with a specific value (O(log n) in balanced BST, O(n) in general tree).

- **Insertion**: Add a new node while maintaining tree properties.

- **Deletion**: Remove a node and restructure the tree if needed.

---

## 3. Complexity Stats
| Operation  | Time(Average) | Time(Worst-Case) | Space     |
| --------   | -------       | --------         | -------   |
| Search (BST) | $O(log n)$  | $O(n)$         | $O(1)$  |
| Insert (BST) | $O(log n)$  | $O(n)$         | $O(1)$  |
| Delete (BST) | $O(log n)$  | $O(n)$         | $O(1)$ |
| Traversal    | $O(n)$      | $O(n)$         |$O(h)$*|

*h = height of tree. For balanced trees, h = log n. For skewed trees, h = n.

---
## 4. Common Problems
This is how you know which tool to grab when you're staring at a problem and drawing a blank.

#### Pattern A: DFS Traversals
- Example Problem: Inorder/Preorder/Postorder Traversal, Path Sum
- Strategy:
    - Use recursion or a stack for iterative approach
    - Inorder: left → root → right (gives sorted order in BST)
    - Preorder: root → left → right (good for copying trees)
    - Postorder: left → right → root (good for deleting trees)

#### Pattern B: BFS / Level Order
- Example Problem: Level Order Traversal, Right Side View
- Strategy:
    - Use a queue to process nodes level by level
    - Track level size to separate levels
    - Process all nodes at current level before moving to next

#### Pattern C: Tree Construction
- Example Problem: Build Tree from Inorder and Preorder
- Strategy:
    - Use one traversal to find root
    - Use another to split left and right subtrees
    - Recursively build left and right subtrees

#### Pattern D: Lowest Common Ancestor
- Example Problem: LCA in Binary Tree, LCA in BST
- Strategy:
    - For BST: use value comparisons to navigate
    - For general tree: recursively search both subtrees
    - LCA is where paths diverge

#### Pattern E: Path Problems
- Example Problem: Path Sum, Binary Tree Maximum Path Sum
- Strategy:
    - Track current path sum as you traverse
    - Use recursion to explore all paths
    - Update global max/result as you go
