class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        answer = 0
        for a in range(0, n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            answer += 1
        return answer
    