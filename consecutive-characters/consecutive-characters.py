class Solution:
    def maxPower(self, s: str) -> int:
        
        
        #Complexity Analysis - O(N) Time and O(1) Space
        
        n = len(s)
        
        if n == 1:
            return 1
        
        answer = 0 #this will hold our output 
        count = 1 #this will count the number of similar consecutive characters
        
        for i in range(0, n-1):
            if s[i] == s[i + 1]:
                count += 1 
            else:
                count = 1 
            answer = max(answer, count)
            
        return answer
        