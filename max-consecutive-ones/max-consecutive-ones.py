class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        count = 0 
        answer = 0 
        for i in nums:
            if i == 1:
                count += 1
                answer = max(answer, count)
            else:
                count = 0 
        return answer