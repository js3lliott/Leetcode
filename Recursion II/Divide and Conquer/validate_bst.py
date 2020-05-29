# Given a binary tree, determine if it is a valid binary search tree (BST)

# Assume a BST is defined as follows:
# 1) The left subtree of a node contains only nodes with keys less than the node's key
# 2) The right subtree of a node contains only nodes with keys greater than the node's key
# 3) Both the left and right subtrees must also be binary search trees

# E.g.      2
#         /   \
#        1     3
# Input: [2, 1, 3]
# Output: True

# E.g.      5
#         /   \
#        1    4
#           /   \
#          3     6
# Input: [5, 1, 4, null, null, 3, 6]
# Output: False
# Explanation: The root node's value is 5 but its right child's value is 4


class TreeNode:
    def _init__(self, x):
        self.val =x
        self.left = None
        self.right = None

class Solution:

    # Recursive Solution
    def isValidBST(self, root: TreeNode):
        def is_bst_helper(root, min_val, max_val):
            if root is None:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            return (is_bst_helper(root.left, min_val, root.val) and is_bst_helper(root.right, root.val, max_val))

        return is_bst_helper(root, float('-inf'), float('inf'))