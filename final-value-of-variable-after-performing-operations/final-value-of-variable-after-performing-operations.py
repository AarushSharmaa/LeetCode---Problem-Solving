class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        #return the final value of X
        #there is a addition and a subtraction operation 
        #Initial value of x is given as 0 
        
        X = 0 
        
        for i in operations:
            
            if i == "++X" or i == "X++":
                X += 1
            else: #if i == "--X" or i == "X--"
                X -= 1
                
        return X
                