# Given a binary array, find the maximum number of consecutive ones
# in this array.

# Example 1:
# Input: [1, 1, 0, 1, 1, 1]
# Output: 3

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0 # create a counter to keep track of consecutive ones
        answer = 0 # keeps track of the maximum consecutive ones

        for num in nums: # loop through the items in the list
            # if we reach a one then we add it to the counter
            # and calculate the max between the current maximum (answer)
            # and the current count else we reset the count of consecutive
            # ones to 0
            if num == 1:
                count += 1
                answer = max(answer, count)
            else:
                count = 0
        return answer