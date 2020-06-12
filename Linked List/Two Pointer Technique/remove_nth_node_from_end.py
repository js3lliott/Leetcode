# Given a linked list, remove the n-th node from the end of the list and return its head.

# Example
# Given linked list: 1 -> 2 -> 3 -> 4 -> 5, and n = 2
# After removing the second node from the end, the linked list becomes 1 -> 2 -> 3 -> 5

# Given n will always be valid

# Could it be done in one pass?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head

        first = second = dummy

        for i in range(n):
            first = first.next

        while first.next is not None:
            first = first.next
            second = second.next

        else:
            second.next = second.next.next

        return dummy.next