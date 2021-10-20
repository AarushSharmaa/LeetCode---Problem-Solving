class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # BRUTE FORCE -- O(N^2) Time and O(1) Space -- Clears 72/89 test cases and then throws TLE
        # generate all subarrays and keep taking their sum 
        # if sum == k, increment count by 1
        
        """
        n = len(nums)
        count = 0 #count of subarrays
        for i in range(0, n):
            add = 0 
            for j in range(i, n):
                add += nums[j]
                if add == k: #as soon as sum of a subarray == k, increment count
                    count += 1
        return count
        """
    
        # Let us think of an O(N) Time approach now
        
        d = {}
        p_sum = 0 
        count = 0 
        d[0] = 1
        n = len(nums)
        
        for i in range(0, n):
            
            p_sum += nums[i]
            
            if (p_sum - k) in d:
                count += d[p_sum - k]
            
            if p_sum in d:
                d[p_sum] += 1
                
            else:
                d[p_sum] = 1
                
        return count