class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #all numbers are in the range of [1,n] inclusive
        #do not modify the array and use O(1) Space
        
        #BRUTE FORCE SOLUTION - O(N^2) Time and O(1) Space -- Throws TLE
        
        """
        n = len(nums)
        for i in range(0, n):
            for j in range(0, n):
                if i != j:
                    if nums[i] == nums[j]:
                        return nums[i]
        """
        
        #APPROACH 2 - O(N*log(N)) and O(1) Space 
        
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return nums[i]
                break
        
        
        
                 
        #OPTIMAL SOLUTION - O(N) Time and O(N) Space -- Accepted
        
        """
        from collections import Counter
        count = Counter(nums)
        for i in count:
            if count[i] != 1:
                return i
        """