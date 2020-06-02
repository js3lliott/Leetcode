# Given a sorted array nums, remove the dupicates in-place such that each element appears only once and return the new length

# Do not allocate extra space for another array, you must do this by modifying the inpur array in-place with O(1) extra memory

# Example 1:
# nums = [1, 1, 2]
# Should return length 2 with the first two elements of nums being 1 and 2

# Example 2:
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Should return length 5 with the five elements being 0, 1, 2, 3, 4

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # We can do a base check to make sure that the array isn't empty
        if len(nums) == 0:
            return 0

        # We can initialize a variable i to be 0 and that will represent the 
        # index 0 (first element)in the array
        i = 0
        # A for loop will be used to loop through the array checking if 
        # the value at nums[j] is equal to nums[i]. If it is then we just skip it.
        # when we find a different element then we insert it into the index specified
        # We keep scanning to find all the unique elements and keep inserting them into the next indices
        # until we are done with the unique elements
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1