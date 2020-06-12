# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position
# (0-indexed) in the linked list where the tail connects to. If pos is -1, then there is no cycle.

# Example 1
# Input: head = [3, 2, 0, -4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the second node.

# Example 2
# Input: head = [1, 2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the first node

# Example 3
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Can it be solved using O(1) (constant) memory?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        # We will be using the two pointer technique with a fast and slow pointer
        # helping us to determine if there is a cycle within the linked list.

        # The fast pointer will taverse the list at twice the speed of the slow
        # pointer, and when the fast pointer is pointing to the same value
        # of the slow pointer then there is a cycle. If not then we will return False

        slow = head
        fast = head.next

        while slow != fast:
            slow = slow.next
            fast = fast.next.next # Skips over two items (twice the speed of the slow pointer)
            return True
        
        return False