class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        #Requirement of the question : 
        
        #This question wants a subarray with an equal number of zeroes and ones - This subarray should be
        #of the maximum length possible among all the eligible subarrays.
        
        #Brute Force --- Throws Time Limit Exceeded
        #Thought Process :
        #We will traverse over the array and consider each subarray one by one. This will need 2 for loops
        #So, time will shoot upto O(N^2)
        
        
        #What the code is doing :
        #First of all, we will fix ith element and then traverse from ith element till the last element
        #Using two separate variables, one representing count of zeroes and other representing count of ones,
        #We will traverse over the entire array and keep updating our valid subarray lengths in an answer variable
        #where we will also ensure to keep track of maximum value
        
        #Complexity Analysis - O(N^2) Time and O(1) Space
        
        """
        n = len(nums)
        answer = 0
        
        for i in range(0, n):
            
            zeroes = 0 #will represent the count of zeroes
            ones = 0 #will represent the count of ones
            
            for j in range(i, n):
                
                if nums[j] == 0:
                    zeroes += 1
                    
                else:
                    ones += 1
                
                #if in a subarray, we have equal number of zeroes and ones
                #we can simply find the length of that subarray
                #and length = j - i + 1
                
                if zeroes == ones: 
                    answer = max(answer, j - i + 1)
                    
        return answer
        """
        
        #Optimal Force - From Discussion Section
        #Thought Process :
        #will update it some time later 
        
        #What the Code is doing :
        #We will iterate over the array and add 1 to count if arr[i] == 1, else add -1
        #If at any point, current == 0, it means our subarray from (0,i) has equal number of 0s and 1s
        #If current != 0, we will check if we have already seen this in d or not
        
        #Complexity Analysis - O(N) Time and O(N) Space
        
        n = len(nums)
        d = {} #a dictionary
        current = 0 #will store the difference of 0s and 1s
        answer = 0 #will store the length of maximum subarray containing equal number of 0s and 1s
        for i in range(0, n):
            
            #if we encounter a 1, we will add 1 to the counter
            if nums[i] == 1:
                current += 1
                
            #if we encounter a 0, we will add -1 to the counter
            else:
                current -= 1
            
            #if the current becomes 0, it means we have covered equal number of 0s and 1s
            #so, subarray in the inclusive range of (0,i) has equal number of 0s and 1s
            #Length of subarray from (0,i) would be (i - 0 + 1) or (i + 1) 
            if current == 0:
                answer = max(answer, i + 1)
            
            #If current != 0 : that means we have got a lot of 1s 
            #or a lot of 0s : basically, current has a non - zero value
            
            #so, we will populate our dictionary with current as keys and index as values
            #so that if we ever encounter repeated values of current, we immediately update our answer
            #and that would be active index - d[current], which will represent the length of the subarray being considered
            
            if current in d:
                answer = max(answer, i-d[current])
            else:
                
                d[current] = i
        
        return answer
        
        