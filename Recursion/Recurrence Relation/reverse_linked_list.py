# Reverse a singly linked list

# Input: 1->2->3->4->5->NULL
# Ouput: 5->4->3->2->1->NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseListRecur(self, head):

        # O(N) time since N is the list's length
        # O(N) space comes from the implicit stack space due to recursion. Recursion could go up to N levels deep

        if not head or not head.next:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node


    def reverseListIter(self, head):

        # O(N) time since N is the list's length
        # O(1) extra space

        prevNode = None
        current = head

        while current != None:
            tempNode = current.next
            current.next = prevNode
            prevNode = current
            current = tempNode

        return prevNode