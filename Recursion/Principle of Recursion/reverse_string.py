# Write a function that reverses a string. The input string is given as an array of characters
# Do not allocate extra space for another array. Must do this by modifying the input array
# in-place with O(1) extra memory.

# Input: ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]

class Solution:
    def reverseStringIter(self, s):
        
        # O(N) time to swap N/2 elements
        # O(1) time, constant space solution
        
        """
        Do not return anything, modify s in-place instead.
        """

        i, j = 0, len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


    def reverseStringRecur(self, s):

        # O(N) tim e to perform N/2 swaps
        # O(N) space to keep the recursion stack

        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)