class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Brute Force Thinking 
        #All test cases passed
        #O(N^2) Time 
        
        
        n = len(s)
        answer = 0 
        for i in range(0, n):
            substring = ""
            d = {}
            for j in range(i, n):
            
        #WAY 1 -- to check if a substring has distinct characters or not
        #This clears 986/987 test cases and then throws TLE at the last test case
        
                substring += s[j]
                if len(set(substring)) == len(substring):
                    answer = max(answer, j - i + 1)
                else:
                    break
        
        #(j - i + 1) simply represents the length of substring being considered 
        #which starts at ith index and ends at jth index
            
        #WAY 2 -- to check if a substring has distinct characters or not
        #This is an accepted solution
        #Remember, looking somethin up in Dictionary is O(1)
                #if (s[j] in d) and (d[s[j]]) > 0 :
                #    break
                #else:
                #    d[s[j]] = 1
                #    answer = max(answer, j - i + 1)
        return answer
        
        
        
        