# Given an array nums and a value val, remove all instances of that value in-place and return the new length

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory
# The order of the elements can be changed. It doesn't matter what you leave beyond the new length

# Example 1:
# Given nums: [3, 2, 2, 3], val = 3
# Should return length = 2 with the first two elements of nums being 2

# Example 2:
# Given nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# Should return length = 5, with the first five elements being 0, 1, 3, 0, 4

class Solution:
    def removeElements(self, nums: List[int], val: int) -> int:
        # Here we will use a two pointer approach with a pointer at the beginning
        # of the array and one at the end of the array. 
        start = 0
        end = len(nums) - 1

        # We can initiate a couple of while loops so that we can check to make sure
        # that they are pointing at the proper indexes.
        # We'll check to see if the pointer pointing to the end of the array is equal
        # to the val that was given and decrease the end by one if it is, which will eliminate the value from the array
        while start <= end:
            while end > start and nums[end] == val:
                end -= 1
            # If the pointer at the beginning of the array is the given val then we can
            # move it to the end of the array and once again decrease the end of the array by 
            # one which will eliminate that value from the array
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            # Increase the starting pointer by one
            start += 1
        # Return the length of the array
        return end + 1
