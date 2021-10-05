class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Brute Force Thinking 
        #Clears 986/987 test cases and then throws TLE
        
        
        n = len(s)
        answer = 0 
        for i in range(0, n):
            #substring = ""
            d = {}
            for j in range(i, n):
            
        #way 1 to check if a substring has distinct characters or n
        
                #substring += s[j]
                #if len(set(substring)) == len(substring):
                    #answer = max(answer, j - i + 1)
            
        #way 2 to check if a substring has distinct characters or not
        
                if s[j] in d:
                    break
                else:
                    d[s[j]] = 1
                    answer = max(answer, j - i + 1)
        return answer
        
        