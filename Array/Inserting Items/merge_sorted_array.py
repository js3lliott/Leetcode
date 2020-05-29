# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array
# Note: 
# The number of elements initialized in nums1 and nums2 are m and n respectively
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2

# Example
# Input: 
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6], n = 3
# Output: [1, 2, 2, 3, 5, 6]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # We can compare the two lists in reverse
        # and put the larger number at the end of nums1
        # If one of the array's is done and has no other elements
        # to compare then the rest is already sorted and we can
        # put them in place in the array

        i = m + n - 1 # iterator on nums1 starting at the end of the full array
        p1 = m - 1 # pointer for nums1 pointing at the end of nums1
        p2 = n - 1 # pointer for nums2 pointing at the end of nums2

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 = p1 - 1
                i = i - 1
            else:
                nums1[i] = nums2[p2]
                p2 = p2 - 1
                i = i - 1
        # Once the array is done we can insert the rest
        nums1[:p2 + 1] = nums2[:p2 + 1]