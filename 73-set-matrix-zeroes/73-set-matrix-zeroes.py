class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        #THIS IS GOING TO BE O(M*N) Time and O(M+N) Space
        
        m = len(matrix) #this is the number of rows
        n = len(matrix[0]) #this is the number of columns
        rows = []
        columns = []
        
        temp = matrix.copy()
        
        hashtable = {}
        
        for r in range(0, m): #this will hold the row
            for c in range(0, n): #this will hold the number of columns 
                if matrix[r][c] == 0:
                    if r not in rows:
                        rows.append(r)
                    if c not in columns:
                        columns.append(c)
        #now, our hashtable contains all the points where 0 was detected in the form of row : column pair
        #and we have to make sure that the elements lying at row i and elements lying at row j are changed to 0
        
        for r in range(0, m):
            for c in range(0, n):
                if r in rows or c in columns:
                    matrix[r][c] = 0 
                
        return matrix
        
        