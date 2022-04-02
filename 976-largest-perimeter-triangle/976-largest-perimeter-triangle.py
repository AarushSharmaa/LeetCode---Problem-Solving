class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        #Without loss of generality, say the sidelengths of the triangle are a <= b <= c
        #The necessary and sufficient condition for these lengths to form a triangle of non-zero area is
        #a + b > c
        
        nums.sort()
        n = len(nums)
        
        temp = 0 
        for i in range(0, n-2):
            if (nums[i] + nums[i+1]) > nums[i+2]:
                perimeter = nums[i] + nums[i+1] + nums[i + 2]
                if perimeter > temp:
                    temp = perimeter
        
        return temp