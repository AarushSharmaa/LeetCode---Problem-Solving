class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        #BRUTE FORCE SOLUTION - Iterate over the entire matrix and see if the target exists 
        #O(M*N) Time and O(1) Space
        
        """
        row = len(matrix)
        column = len(matrix[0])
        
        for r in range(0, row): 
            for c in range(0, column):
                if matrix[r][c] == target:
                    return True 
        """
        
        #Obviously we need to think in terms of Binary Search, as we know that the array is already sorted 
        
        for array in matrix:
            left = 0 
            right = len(array) - 1
            while left <= right:
                mid = (left + right) // 2
                if target == array[mid]: 
                    return True
                elif target > array[mid]:
                    left += 1 
                else:
                    right -= 1
            