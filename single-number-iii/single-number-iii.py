class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        
        #two elements appear only once and all others appear exactly twice
        #find two elements that appear only once
        #order of answer does not matter
        
        
        #APPROACH 1 : O(N) Time and O(N) Space
        
        
        d = {} #this will contain elements corresponding to its frequency 
        answer = [] #this will hold our answer
        
        #let us populate our hashtable now
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for element in d:
            if d[element] == 1: #it means frequency of element is 1
                answer.append(element)
        return answer
         
        