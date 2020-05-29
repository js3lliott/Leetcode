class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoListsRecur(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        elif (l1.val < l2.val):
            l1.next = self.mergeTwoListsRecur(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecur(l1, l2.next)
            return l2

        # Time Complexity: O(n + m)
        # Because each recursive call increments the pointer to l1 or l2 by one (approaching the
        # dangling null at the end of each list), there will be exactly one call to mergeTwoListsRecur
        # per element in each list. Therefore, the time complexity is linear in the combined size
        # of the lists

        # Space Complexity: O(n + m)
        # The first call to mergeTwoListsRecur does not return until the ends of both l1 and l2
        # have been reached, so n + m stack frames consume O(n + m) space

    
    def mergeTwoListsIter(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list
        prev.next = l1 or l2
            
        return prehead.next

        # Time Complexity: O(n + m)
        # Because exactly one fo l1 and l2 is incremented on each loop iteration, the while loop runs
        # for a number of iterations equal to the sum of the lengths of the two lists. ALl other
        # work is constant, so the overall complexity is linear

        # Space Complexity: O(1)
        # The iterative approach only allocates a few pointers, so it has constant overall
        # memory footprint