"""
dynamic_programming.py

A collection of common DP patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

from typing import List

# ---------------------------------------------------------
# Pattern A: 1D DP (Fibonacci Style)
# ---------------------------------------------------------

def climb_stairs(n: int) -> int:
    """
    Calculates number of ways to climb n stairs taking 1 or 2 steps.
    Time: O(n)
    Space: O(1)
    """
    if n <= 2:
        return n
        
    prev1, prev2 = 2, 1
    
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
        
    return prev1

# ---------------------------------------------------------
# Pattern B: 2D DP (0/1 Knapsack Style)
# ---------------------------------------------------------

def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Finds the maximum value that can be put in a knapsack of given capacity.
    Time: O(n * capacity)
    Space: O(capacity)
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
            
    return dp[capacity]

# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------

if __name__ == "__main__":
    print(climb_stairs(5))  # 8
    
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    print(knapsack(weights, values, capacity))  # 22
