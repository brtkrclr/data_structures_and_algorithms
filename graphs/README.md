# 📌 Graphs

## 1. Basic Information

**Definition**: A graph is a non-linear data structure consisting of nodes (vertices) and edges that connect these nodes.

**Physical Representation**: Usually represented as an Adjacency List (a dictionary or array of lists) or an Adjacency Matrix (a 2D grid).

**Key Analogy**: Think of it like a road map. Cities are vertices, and the roads connecting them are edges.

**In Python:**  
- Implemented using `dict` (hash map) where keys are nodes and values are lists of neighbors.
- Alternatively, using `list` of `list`s for an adjacency matrix.

**When to Use Graphs:**  
- Network routing
- Social networks
- Finding shortest paths
- Dependency resolution

---

## 2. Basic Operations

- **Add Vertex**: Inserting a new node into the graph.
- **Add Edge**: Connecting two existing vertices.
- **Traversal (BFS/DFS)**: Visiting all the nodes in the graph in a specific order.

---

## 3. Complexity Stats
| Operation  | Time (Adjacency List) | Space |
| --------   | ------- | ------- |
| Add Vertex | $O(1)$ | $O(1)$ |
| Add Edge   | $O(1)$ | $O(1)$ |
| BFS/DFS    | $O(V + E)$ | $O(V)$ |

---
## 4. Common Problems

#### Pattern A: Breadth-First Search (BFS)
- Example Problem: Shortest Path in Unweighted Graph
- Strategy: Use a queue to explore level by level.

#### Pattern B: Depth-First Search (DFS)
- Example Problem: Number of Islands
- Strategy: Use recursion or a stack to explore as far as possible along each branch.
