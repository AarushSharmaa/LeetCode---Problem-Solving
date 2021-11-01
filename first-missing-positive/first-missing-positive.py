class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        

        
        n = len(nums)
        
        #if size is n, nums should have numbers in the range of [1,n] inclusive 
        #so, if an integer is missing, it should be in the range of [1,n] inclusive
        
        d = {}
        
        #populating the dictionary with elements as the keys
        #as lookups in dictionary will take O(1) Time
        for i in nums:
            d[i] = 0 
        
        for i in range(1, n+1):
            if i not in d:
                return i 
        else:
            return i + 1