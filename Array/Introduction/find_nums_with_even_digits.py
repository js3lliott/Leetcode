# Given an array nums of integers, return how many of them contain
# an even number of digits

# Example 1
# Input: [12, 345, 2, 6, 7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits)
# 345 contains 3 digits (odd)
# 2 contains 1 digit (odd)
# 6 contains 1 digit (odd)
# 7896 contains 4 digits (even)
# Therefore only 12 and 7896 contain an even number of digits

# Example 2
# Input: [555, 901, 482, 1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([x for x in nums if len(str(x)) % 2 == 0])