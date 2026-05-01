# 📌 Dynamic Programming

## 1. Basic Information

**Definition**: An algorithmic paradigm that solves a complex problem by breaking it down into simpler overlapping subproblems and storing the results to avoid redundant computations.

**Physical Representation**: Usually stored in an array (1D DP) or a matrix (2D DP) for tabulation, or a hash map/memoization array for top-down recursion.

**Key Analogy**: If I ask you what 1+1+1+1+1+1+1+1 is, you count and say 8. If I add another +1 to the end, you immediately say 9 because you remembered the previous answer rather than recounting from the beginning.

**In Python:**  
- Top-down uses recursive functions with `@cache` or `@lru_cache(None)` from the `functools` module.
- Bottom-up uses `list` arrays or `list` of `list`s matrices.

**When to Use Dynamic Programming:**  
- The problem asks for the optimal solution (max/min), total ways, or if something is possible.
- The problem has overlapping subproblems and optimal substructure.

---

## 2. Basic Approaches

- **Top-Down (Memoization)**: Start from the target state and recursively calculate sub-states, saving results to avoid recalculating.
- **Bottom-Up (Tabulation)**: Start from the base cases and iteratively build up to the target state.

---

## 3. Complexity Stats
| Problem    | Time        | Space       |
| --------   | -------     | -------     |
| 1D DP      | $O(n)$      | $O(n)$ or $O(1)$ |
| 2D DP      | $O(n \times m)$| $O(n \times m)$ or $O(\min(n, m))$ |

---
## 4. Common Problems

#### Pattern A: Fibonacci Sequence
- Example Problem: Climbing Stairs
- Strategy: dp[i] = dp[i-1] + dp[i-2]

#### Pattern B: 0/1 Knapsack
- Example Problem: Partition Equal Subset Sum
- Strategy: Choose whether to include an item or not, updating a 2D array or optimized 1D array.
