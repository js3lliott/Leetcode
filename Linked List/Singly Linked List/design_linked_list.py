# Design your implementation of the linked list. you can choose to use the singly
# linked list or doubly linked list. A node in a singly linked list should have
# two attributes: val and next. val is the value of the current node, and next
# is a pointer/reference to the next node. If you want to use the doubly linked list, 
# you will need one more attribute prev to indicate the previous node in the linked
# list. Assume all nodes in the linked list are 0-indexed

# Implement these functions in your linked list class:
# get(index): Get the value of the index-th node in the linked list. If the index is invalid return -1
# addAtHead(val): Add a node of value val before the first element of the linked list.
# After the insertion, the new node will be the first node of the linked list
# addAtTail(val): Append a node of value val to the last element of the linked list
# addAtIndex(index, val): Add a node of value val before the index-th node in the linked list.
# If index equals to the length of the linked list, the node will be appended to the end of
# the linked list, If the index is greater than the length, the node will not be inserted
# deleteAtIndex(index): Delete the index-th node in the linked list, if the index is valid

# Example:
# Input: 
# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]
# Output:  
# [null,null,null,null,2,null,3]

# Explanation:
# MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize the data here
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion,
        the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)

        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1

    def addAtIndex(self, index: int, val:int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals 
        the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """

        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)

        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            newNode = Node(val)
            newNode.next = curr.next
            curr.next = newNode

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next

        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        
        self.size -= 1