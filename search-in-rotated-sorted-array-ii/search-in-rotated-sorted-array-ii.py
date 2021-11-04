class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        #BRUTE FORCE : Linear Search
        
        if target in nums:
            return True
        
        """
        
        d = {}
        for i in nums:
            d[i] = 0 
        
        if target in d:
            return True
        else:
            return False
        
        """