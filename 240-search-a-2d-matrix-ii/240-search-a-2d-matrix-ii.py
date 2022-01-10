class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        row = len(matrix)
        column = len(matrix[0])
        
        for r in range(0, row):
            for c in range(0, column):
                if matrix[r][c] == target:
                    return True 
                