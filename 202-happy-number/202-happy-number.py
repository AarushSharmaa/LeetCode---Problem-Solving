class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        #clears 402/404 test cases

        while len(str(n)) > 1:
            s = str(n)
            add = 0
            for i in s:
                add += (int(i) ** 2) 
            n = add 
        
        if n == 1 or n == 7:
            return True
        
        
        