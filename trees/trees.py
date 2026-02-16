"""
trees.py

A collection of common tree patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    """Binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------------------------------------------------------
# Pattern A: DFS Traversals
# ---------------------------------------------------------

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Inorder traversal: left → root → right
    Time: O(n)
    Space: O(h) where h is height
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Preorder traversal: root → left → right
    Time: O(n)
    Space: O(h)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Postorder traversal: left → right → root
    Time: O(n)
    Space: O(h)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    
    dfs(root)
    return result


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Iterative inorder traversal using a stack.
    Time: O(n)
    Space: O(h)
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result


# ---------------------------------------------------------
# Pattern B: BFS / Level Order
# ---------------------------------------------------------

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal (BFS).
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    Returns the values visible from the right side of the tree.
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Add the last node of each level
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result


# ---------------------------------------------------------
# Pattern C: Tree Properties
# ---------------------------------------------------------

def max_depth(root: Optional[TreeNode]) -> int:
    """
    Finds the maximum depth of a binary tree.
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    Checks if a binary tree is height-balanced.
    Time: O(n)
    Space: O(h)
    """
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return check_height(root) != -1


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Checks if two trees are identical.
    Time: O(n)
    Space: O(h)
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))


# ---------------------------------------------------------
# Pattern D: Path Problems
# ---------------------------------------------------------

def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    """
    Checks if there's a root-to-leaf path with given sum.
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == target_sum
    
    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))


def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    Finds the maximum path sum in a binary tree.
    Time: O(n)
    Space: O(h)
    """
    max_sum = float('-inf')
    
    def max_gain(node):
        nonlocal max_sum
        
        if not node:
            return 0
        
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Path through current node
        current_path = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path)
        
        # Return max gain if we continue the path
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum


# ---------------------------------------------------------
# Pattern E: BST Operations
# ---------------------------------------------------------

def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Searches for a value in a BST.
    Time: O(h)
    Space: O(1)
    """
    current = root
    
    while current:
        if val == current.val:
            return current
        elif val < current.val:
            current = current.left
        else:
            current = current.right
    
    return None


def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Inserts a value into a BST.
    Time: O(h)
    Space: O(1)
    """
    if not root:
        return TreeNode(val)
    
    current = root
    
    while True:
        if val < current.val:
            if not current.left:
                current.left = TreeNode(val)
                break
            current = current.left
        else:
            if not current.right:
                current.right = TreeNode(val)
                break
            current = current.right
    
    return root


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Validates if a tree is a valid BST.
    Time: O(n)
    Space: O(h)
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))


# ---------------------------------------------------------
# Pattern F: Lowest Common Ancestor
# ---------------------------------------------------------

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor of two nodes.
    Time: O(n)
    Space: O(h)
    """
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right


# ---------------------------------------------------------
# Example Usage (for local testing)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Create a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Inorder: {inorder_traversal(root)}")      # [4, 2, 5, 1, 3]
    print(f"Preorder: {preorder_traversal(root)}")    # [1, 2, 4, 5, 3]
    print(f"Postorder: {postorder_traversal(root)}")  # [4, 5, 2, 3, 1]
    print(f"Level order: {level_order(root)}")        # [[1], [2, 3], [4, 5]]
    print(f"Max depth: {max_depth(root)}")            # 3
    print(f"Is balanced: {is_balanced(root)}")        # True
    print(f"Right side view: {right_side_view(root)}")  # [1, 3, 5]
