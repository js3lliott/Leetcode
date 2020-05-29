class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if (not matrix or not matrix[0]):
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        i = 0
        j = 0
        
        result = []
        
        for k in range(0, rows * cols):
            result.append(matrix[i][j])
            
            if ((i + j) % 2 == 0):
                if (j == cols - 1):
                    i += 1
                elif (i == 0):
                    j += 1
                else:
                    i -= 1
                    j += 1
                    
            else:
                if (i == rows - 1):
                    j += 1
                elif (j == 0):
                    i += 1
                else:
                    i += 1
                    j -= 1
                    
        return result