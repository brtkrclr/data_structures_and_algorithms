"""
linked_lists.py

A collection of common linked list patterns used in interviews and LeetCode,
implemented as small, focused functions.
"""

from typing import Optional


class ListNode:
    """Standard singly linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------------------------------------------------------
# Pattern A: Two Pointers (Fast & Slow)
# ---------------------------------------------------------

def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detects if a linked list has a cycle.
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Finds the middle node of a linked list.
    If even length, returns the second middle node.
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


# ---------------------------------------------------------
# Pattern B: Reversal
# ---------------------------------------------------------

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverses a linked list iteratively.
    Time: O(n)
    Space: O(1)
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverses a linked list recursively.
    Time: O(n)
    Space: O(n) due to recursion stack
    """
    if not head or not head.next:
        return head
    
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head


# ---------------------------------------------------------
# Pattern C: Merge & Combine
# ---------------------------------------------------------

def merge_two_sorted_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merges two sorted linked lists into one sorted list.
    Time: O(n + m)
    Space: O(1)
    """
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2
    
    return dummy.next


# ---------------------------------------------------------
# Pattern D: In-place Modification
# ---------------------------------------------------------

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Removes the nth node from the end of the list.
    Time: O(n)
    Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    
    first = second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node
    second.next = second.next.next
    
    return dummy.next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Removes duplicates from a sorted linked list.
    Time: O(n)
    Space: O(1)
    """
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


# ---------------------------------------------------------
# Pattern E: Runner Technique
# ---------------------------------------------------------

def reorder_list(head: Optional[ListNode]) -> None:
    """
    Reorders list from L0→L1→...→Ln-1→Ln to L0→Ln→L1→Ln-1→L2→Ln-2...
    Time: O(n)
    Space: O(1)
    """
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second = slow.next
    slow.next = None
    second = reverse_list(second)
    
    # Merge two halves
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def create_linked_list(values: list) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Helper function to convert a linked list to a Python list."""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


# ---------------------------------------------------------
# Example Usage (for local testing)
# ---------------------------------------------------------

if __name__ == "__main__":
    # Test cycle detection
    head = create_linked_list([1, 2, 3, 4, 5])
    print(f"Has cycle: {has_cycle(head)}")  # False
    
    # Test finding middle
    middle = find_middle(head)
    print(f"Middle value: {middle.val}")  # 3
    
    # Test reversal
    reversed_head = reverse_list(head)
    print(f"Reversed list: {linked_list_to_list(reversed_head)}")  # [5, 4, 3, 2, 1]
    
    # Test merge
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    merged = merge_two_sorted_lists(l1, l2)
    print(f"Merged list: {linked_list_to_list(merged)}")  # [1, 2, 3, 4, 5, 6]
