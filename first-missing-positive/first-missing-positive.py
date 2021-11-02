class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        #BRUTE FORCE SOLUTION
        """
        n = len(nums)
        
        for i in range(1, n+1):
            if i not in nums:
                return i
        return i + 1
        """
        
        #OPTIMAL SOLUTION
        
        n = len(nums)
        
        #if size is n, nums should have numbers in the range of [1,n] inclusive 
        #so, if an integer is missing, it should be in the range of [1,n] inclusive
        
        d = {}
        
        #populating the dictionary with elements as the keys
        #as lookups in dictionary will take O(1) Time
        #values corresponding to elements don't really matter
        for i in nums:
            d[i] = 0 
        
        
        for i in range(1, n+1):
            if i not in d: #this will not take O(N) Time but will take O(1) Time only
                #as lookups in Hashtables are much faster than lookups in an array
                return i 
        return i + 1
        