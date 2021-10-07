class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        
        n = len(nums)
        
        count_increasing = 0
        count_decreasing = 0
        
        #If the array is monotonic increasing
        for i in range(1, n):
            if nums[i] >= nums[i-1]:
                count_increasing += 1
                
        #If the array is monotonic decreasing
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                count_decreasing += 1
        
        #For an array with 4 elements, there will be 3 comparisons
        
        if count_increasing == n - 1 or count_decreasing == n - 1:
            return True