class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        #first, find the degree (maximum ferquency of one of its elements)
        #then, find all the subarrays of size with same "degree" and return the length of smallest such subarray
        
        
        #alternatively, find the first occurence of the element and the last occurence of the element 
        #this will return the smallest possible length of a subarray of nums that has same degree as that of nums
        #above case works only if there is 1 element with the highest frequency
        
        from collections import Counter
        count = Counter(nums) #count holds elements and their frequencies
        arr1 = [] 
        for i in count:
            arr1.append(count[i]) #this array holds the frequency of all elements
        degree = max(arr1) #degree of an array 
        
        arr = []
        for i in count:
            if count[i] == degree:
                arr.append(i) #this holds the element having degree frequency
        
        n = len(nums)
        
        if len(arr) == 1: #if there is only one element with highest frequency
            for j in range(n-1, -1, -1):
                if nums[j] == arr[0]:
                    last_point = j 
                    break
            for i in range(0, n):
                if nums[i] == arr[0]:
                    first_point =  i
                    break
            answer = last_point - first_point + 1
            return answer
        
        else:
            answer = 9999999 
            for element in arr:
                for j in range(n-1, -1, -1):
                    if nums[j] == element:
                        lp = j 
                        break 
                        
                for i in range(0, n):
                    if nums[i] == element:
                        fp = i 
                        break 
                        
                answer = min(answer, lp - fp + 1)
            return answer
            
        
           
                    
        