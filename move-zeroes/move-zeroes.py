class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Approach 1 : O(N) Time and O(N) Space
        
        #First, create a copy and iterate over the created copy
        #as soon as we find 0, add it to a separate array and remove it from the given array
        #at the end, just add the separate array containing all zeroes to the given array
        
        """
        temp = nums.copy()
        a = []
        for i in temp:
            if i == 0:
                a.append(i)
                nums.remove(i)
        nums.extend(a)
        return nums
        """
        
        #Approach 2 :
        
        n = len(nums)
        #if we start at 0th index, last index would be (n-i-1)th index
        if n == 1:
            return nums 
        
        for i in range(0, n):
            if nums[i] == 0:   #check if the number is zero (if yes)
                nums.append(0) #add zero to the end of the list
                nums.remove(0) #remove the first zero found (from left)
        return nums
        
        
        
            
        