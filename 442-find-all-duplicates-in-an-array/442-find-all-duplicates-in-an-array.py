class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        #return an array of all integeres that appears twice
        #nums is in the range of [1,n] inclusive
        
        
        #Approach 1 : O(N) Time and O(N) Space 
        
        #first, we will remove all the elements of nums
        #then, we will iterate over the frequency dictionary and return all the elements whose frequency == 2
        
        """
        from collections import Counter
        c = Counter(nums) #this creates a dictionary of elements corresponding to its frequency in the given array
        
        temp = nums.copy()
        
        
        for i in temp:
            nums.remove(i)
        
        for i in c:
            if c[i] == 2:
                nums.append(i)
        return nums
        """
        
        answer = [] #will hold our final answer
        d = {} #will hold elements corresponding to its frequency in the form of key-value par
        
        #let us populate our dictionary now
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for element in d:
            if d[element] == 2:
                answer.append(element)
                
        return answer