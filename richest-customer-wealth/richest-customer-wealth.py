class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        #O(N^2) Time and O(1) Space
        

        answer = 0
        for i in range(0, len(accounts)): #this will fix our row or the customer
            wealth = 0 
            for j in range(0, len(accounts[0])): #this will fix our column or banks for a specific customer
                wealth += accounts[i][j]
            answer = max(answer, wealth)
        return answer
    
        #to access the number of rows or to fix rows - use code : for i in range(0, len(matrix))
        #to access the number of columns or to fix colums - use code : for j in range(0, len(matrix[0]))