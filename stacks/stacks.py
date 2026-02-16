"""
stacks.py

A collection of common stack patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

from typing import List


# ---------------------------------------------------------
# Pattern A: Balanced Parentheses
# ---------------------------------------------------------

def is_valid_parentheses(s: str) -> bool:
    """
    Checks if a string of parentheses is valid.
    Time: O(n)
    Space: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack


def min_remove_to_make_valid(s: str) -> str:
    """
    Removes minimum number of parentheses to make string valid.
    Time: O(n)
    Space: O(n)
    """
    stack = []
    s_list = list(s)
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s_list[i] = ''
    
    # Remove unmatched opening parentheses
    while stack:
        s_list[stack.pop()] = ''
    
    return ''.join(s_list)


# ---------------------------------------------------------
# Pattern B: Monotonic Stack
# ---------------------------------------------------------

def next_greater_element(nums: List[int]) -> List[int]:
    """
    Finds the next greater element for each element in the array.
    Time: O(n)
    Space: O(n)
    """
    result = [-1] * len(nums)
    stack = []
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    Returns how many days until a warmer temperature.
    Time: O(n)
    Space: O(n)
    """
    result = [0] * len(temperatures)
    stack = []
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    
    return result


# ---------------------------------------------------------
# Pattern C: Expression Evaluation
# ---------------------------------------------------------

def eval_rpn(tokens: List[str]) -> int:
    """
    Evaluates Reverse Polish Notation expression.
    Time: O(n)
    Space: O(n)
    """
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    
    return stack[0]


def basic_calculator(s: str) -> int:
    """
    Evaluates a basic arithmetic expression with +, -, and parentheses.
    Time: O(n)
    Space: O(n)
    """
    stack = []
    operand = 0
    result = 0
    sign = 1
    
    for char in s:
        if char.isdigit():
            operand = operand * 10 + int(char)
        elif char == '+':
            result += sign * operand
            sign = 1
            operand = 0
        elif char == '-':
            result += sign * operand
            sign = -1
            operand = 0
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * operand
            result *= stack.pop()
            result += stack.pop()
            operand = 0
    
    return result + sign * operand


# ---------------------------------------------------------
# Pattern D: Min/Max Stack
# ---------------------------------------------------------

class MinStack:
    """
    Stack that supports push, pop, top, and retrieving minimum in O(1).
    """
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    
    def get_min(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


# ---------------------------------------------------------
# Pattern E: Stack-based DFS
# ---------------------------------------------------------

def dfs_iterative(graph: dict, start: int) -> List[int]:
    """
    Performs iterative DFS using a stack.
    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add neighbors in reverse order for correct traversal
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


# ---------------------------------------------------------
# Example Usage (for local testing)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Test valid parentheses
    print(is_valid_parentheses("()[]{}"))  # True
    print(is_valid_parentheses("([)]"))    # False
    
    # Test next greater element
    print(next_greater_element([2, 1, 2, 4, 3]))  # [4, 2, 4, -1, -1]
    
    # Test daily temperatures
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
    
    # Test RPN evaluation
    print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9
    
    # Test MinStack
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.get_min())  # -3
    min_stack.pop()
    print(min_stack.top())      # 0
    print(min_stack.get_min())  # -2
