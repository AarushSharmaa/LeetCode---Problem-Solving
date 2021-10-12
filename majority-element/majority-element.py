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
        
        
        