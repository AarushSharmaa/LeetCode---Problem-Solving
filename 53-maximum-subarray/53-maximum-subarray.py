class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #BRUTE FORCE - O(N^2) Time and O(1) Space
        #note - this array contains negative numebrs as well
        
        #subarray - contiguous part of an array, and relative ordering must be maintained
        
        """
        answer = -9999999999999999999999
        for i in range(0, len(nums)):
            subarray_sum = 0 
            for j in range(i, len(nums)):
                subarray_sum += nums[j]
                answer = max(answer, subarray_sum)
        return answer
        """
        
        #O(N) Time and O(1) Space
        
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] = nums[i] + nums[i-1]
        return max(nums)