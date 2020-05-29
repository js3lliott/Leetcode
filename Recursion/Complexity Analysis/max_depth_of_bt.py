# Given a binary tree, find its maximum depth
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: a leaf is a node with no children

# Given a binary tree: [3, 9, 20, null, null, 15, 7]
    #     3
    #   /   \
    #  9    20
    #      /  \
    #     15   7
# Return its depth = 3


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode):
        if root == None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1