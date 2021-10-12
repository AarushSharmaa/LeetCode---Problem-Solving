class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        c0 = 0  #count of number of zeroes
        c1 = 0  #count of number of ones
        c2 = 0  #count of number of twos
        
        for i in nums:
            if i == 0:
                c0 += 1
                
            elif i == 1:
                c1 += 1
                
            else:
                c2 += 1
                
        for i in range(0, c0):
            nums[i] = 0 
            
        for i in range(c0, c0 + c1):
            nums[i] = 1
            
        for i in range(c0 + c1, c0 + c1 + c2):
            nums[i] = 2
        return nums