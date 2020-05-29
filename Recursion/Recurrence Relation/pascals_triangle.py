# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle
# In Pascal's triangle, each number is the sum of the two numbers directly above it
#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1

# Input: 5
# Ouput: [
#       [1],
#     [1, 1],
#    [1, 2, 1],
#   [1, 3, 3, 1],
#  [1, 4, 6, 4, 1]
# ]

class Solution:
    def generate(self, numRows):

        result = [[1] * (i+1) for i in range(numRows)]

        for i in range(numRows):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result [i -1 1][j]
        return result




    def generateIterDynamic(self, numRows):
        
        # O(numRows^2) time
        # O(numRows^2) space because we need to store each number that we update in triangle, so space is same as time complexity
        
        triangle = []

        for row_num in range(numRows):
            # the first and last row elements are always 1
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            triangle.append(row)

        return triangle