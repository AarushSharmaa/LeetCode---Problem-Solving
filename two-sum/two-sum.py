class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Brute Force way of thinking
        #Generate all subarrays and as soon as we find the condition getting fulfilled, append it to our answer
        #Note - as per question, only 1 valid answer exists, so repetition will not be an issue
        #If at all there was repetition, it can be avoided by traversing as below
        #O(N^2) Time -- Accepted Solution
        
        """
        n = len(nums)
        answer = list()
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i] + nums[j] == target):
                    answer.append(i)
                    answer.append(j)
        return answer        
        """
        
        #Let us try two pointers approach
        
        #NOTE - We CANNOT SORT THIS array as we have to retrieve the indices and sorting it 
        #would change the original indices at which elements are present
        #If the given array would have already been sorted, this would have worked completely fine
        
        #if we fix one of the numbers as arr[i], so other would be arr[j] = (target - arr[i]) 
        #now, we simply have to see if this arr[j] exists in the given array or not
        #O(N) Time --- Accepted Solution (TAKEN HELP FROM DISCUSSION SECTION)
        
        #NOTE - Looking up an element in a dictionary is O(1) and not O(N) 
        """
        
        n = len(nums)
        seen = {} #empty dictionary

        for index, value in enumerate(nums): 
            
            remaining = target - value 
            #here, value is nums[i]
            #we are looking for this remaining, which is nums[j] 
            #we have to find if remaining or nums[j] is present in the given array or not
            #this equation comes from the fact that as per question : 
            #nums[i] + nums[j] = target 
           
            if remaining in seen: 
                
                #if nums[j] is present in dictionary
                #just return index of nums[i] and nums[j] 
                return [index, seen[remaining]] 
                #index represents index of nums[i] and seen[remaining] will
                #hold index of nums[j]
            
            else: 
            #otherwise, add the value corresponding to its index in the dictionary
            #so, if it searched again, we can directly retrieve its index
                seen[value] = index 
                
        """
        n = len(nums)
        d = {}
        output = []
        
        for i in range(0, n):
            d[nums[i]] = i
            
        for i in range(0, n):
            remaining = target - nums[i]
            if remaining in d and i != d[remaining]:
                output.append(i)
                output.append(d[remaining])
                break
        return output
                