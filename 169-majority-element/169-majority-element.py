class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #majority element is the element that appears more than ⌊n / 2⌋ times
        #It is to be noted that majority element always exists in the array
        
        
        #Time Consumed - O(N) and Space Consumed - O(N)
        
        
        n = len(nums)
        frequency_required = n//2
        
        #if an element occurs more than frequency, return it
        
        #This dictionary will hold elements and their frequency in the form of key - value pair
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for element in d:
            if d[element] > frequency_required:
                return element 
        
        
        """
        #O(N^2) Time and O(1) Space
        
        
        n = len(nums)
        frequency = n // 2
        
        if n == 1:
            return nums[0]
        
        #we need the element that appears more than frequency times in the array -- that will be our majority element
        
        for i in range(0, n):
            occurence = 1
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    occurence += 1
                    if occurence > frequency:
                        return nums[i]
        """      
        
        