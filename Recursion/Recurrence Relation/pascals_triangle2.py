# Given a non-negative index k where k <= 33, return the kth index row of Pascal's triangle
# Row index starts from 0

class Solution:

    def getRow(self, rowIndex):
        row = [1]

        for i in range(1, rowIndex + 1):
            row = [1] + [row[i] + row[j + 1] for j in range(len(row) - 1)] + [1]
        return row