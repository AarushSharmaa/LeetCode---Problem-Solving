class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        #product of its digits
        product = 1 
        for i in str(n):
            product = product * int(i)
        
        #sum of its digits 
        add = 0 
        for i in str(n):
            add = add + int(i)
        
        ans = product - add
        return ans
        