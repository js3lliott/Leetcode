# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1 -> 2 -> 4, 1 -> 3 -> 4
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        prev_head = ListNode(-1)
        curr = prev_head

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return prev_head.next


    def mergeTwoListsRecur(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoListsRecur(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecur(l1, l2.next)
            return l2
