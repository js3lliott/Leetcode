# Given a linked list, swap every two adjacent nodes and return its head

# Example: Given 1 -> 2 -> 3 -> 4, you should return list as 2 -> 1 -> 4 -> 3


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairsRecur(self, head):

        # O(N) time where N is the size of the linked list
        # O(N) space for the stack space utilized for recursion

        # If the list has no node or has only one node left 
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        firstNode = head
        secondNode = head.next

        # Swapping
        firstNode.next = self.swapPairs(secondNode.next)
        secondNode.next = firstNode

        # Now the head is the second node
        return secondNode



    def swapPairsIter(self, head):

        # O(N) time where N is the size of the linked list
        # O(1) space

        # We create a Dummy node that acts as the prevNode for the head node
        # of the list and hence stores the pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prevNode = dummy

        while head and head.next:

            # Nodes to be swapped
            firstNode = head
            secondNode = head.next

            # Swapping
            prevNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode

            # Reinitializing the head and prevNode for the next swap
            prevNode = firstNode
            head = firstNode.next
        # Return the new head node
        return dummy.next