class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
       
        #Time Consumed - O(N) and Space Consumed - O(N)
        #In comments, we have taken the first test case
        
        """
        from collections import Counter
        frequency = Counter(nums) #Counter({2: 2, 1: 1, 3: 1}) 
        add = 0
        
        for i in frequency: 
            if frequency[i] == 1: 
            #we will retrieve all elements whose frequency is 1
            #and add it to our "add" variable 
                add += i 
        return add 
        """
        
        #Let us try to optimise it - Since Time Complexity looks decent, let us try to reduce the space to O(1)
        #Basic idea is to retrieve all the elements that appeared only once and find their sum
        
        n = len(nums)
        answer = 0
        for i in range(0, n): #nums[i] will be our fixed character at each iteration
            count = 0 #this will count the number of characters not similar to the fixed character
            for j in range(0, n): #we will check if nums[i] == nums[j] at any point
                if i != j:
                    if nums[i] != nums[j]:
                        count += 1
            if count == n - 1:
                answer += nums[i]
            
        return answer   