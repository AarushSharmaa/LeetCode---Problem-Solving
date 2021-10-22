class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        #A brute Force Approach - Sort the array and then check the consecutiveness present in an array
        #And keep updating them in a separate variable - It will cost O(Nlog(N)) Time and O(1) Space
        
        #This fails  at [1,2,0,1]. Required output is 3 [due to 0,1,2] --> 
        #But as per code flow, once we sort it, we will have [0,1,1,2]. And as per below code, our output is 2. 
        
        
        nums.sort() #pre-computation
        
        n = len(nums)
        
        if n == 0:
            return 0 
        
        if n == 1:
            return 1
        
        arr = []
        arr.append(nums[0])
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                arr.append(nums[i])
                
        longest_streak = 1
        current_streak = 1
        
        n1 = len(arr)
        for i in range(1, n1):
            
            if arr[i] == arr[i-1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
                
        #for cases like [1,2,3,4,101,102,103,104,105]
        #the last set of consecutive elements from 101 to 105 will not be updated in the
        #longest_streak variable, so we will take max of both these to get desired output
        return max(longest_streak, current_streak)
        
        
        #Lets think from more even more basics to get a solution before we move to optimising it
        #Note - we have been asked what is the longest consec
        