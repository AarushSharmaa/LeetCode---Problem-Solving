class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #it handles integer overflows
        """
        left = 0 
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left)//2 
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            
            if nums[mid] > target:
                right = mid - 1 
                
        return -1
        """
        
        #it does not handle integer overflow
        """
        left = 0 
        n = len(nums)
        right = n - 1
        
        while left <= right:
            
            mid = (left + right)// 2
            
            if nums[mid] == target:
                return mid 
            
            if  target < nums[mid]:
                right = mid - 1
                
            elif target > nums[mid]:
                left = mid + 1
                
        return -1
        """
        
        left = 0 
        n = len(nums)
        right = n - 1
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            
            if nums[mid] < target:
                left = mid + 1
        
        return -1