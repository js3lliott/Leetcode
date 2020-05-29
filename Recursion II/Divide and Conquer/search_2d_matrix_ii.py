# Write an efficient algorithm that searches for value in an m x n matrix. This matrix has the following properties:
# 1) Integers in each row are sorted in ascending from left to right
# 2) Integers in each column are sorted in ascending from top to bottom

# E.g.  
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]      
# ]
# Given target = 5, return True
# Given target = 20, return False


class Solution:

    def searchMatrix(self, matrix, target):

        if not matrix:
            return False

        height = len(matrix)
        width = len(matrix[0])

        row = height - 1
        col = 0

        while row >= 0 and col < width:
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                row -= 1

            else:
                col += 1

        return False