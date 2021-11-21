class Solution:
    def numSub(self, s: str) -> int:
        
        #Brute Force Approach -- Clears 53/56 test cases and then throws TLE
        #Traverse over each substring and if the substring contains only 1
        #increment our answer, which we will initialise to 0 in the beginning
        #O(N^2) Time and O(N) Space
        
        """
        
        n = len(s)
        answer = 0  #will contain number of substrings that has the character 1 
        
        for i in range(0, n): 
            substring = ""
            for j in range(i, n):
                substring += s[j]
                
                #If the substring contains 1 and no other character
                #then, the length of the set(substring) will be 1 as set removes all duplicates
                #If there would have been 0, below condition will not be satisfied
                #Else, we will break out and not consider any other substring beyond it as it already contains 
                #a character that is not 1
                
                if "1" in substring and len(set(substring)) == 1:
                    answer += 1
                else:
                    break
                    
        return answer % (10**9 + 7)
        
        """
        
        #Lets think of some optimization now, majorly in terms of time
        #Reading the hints - if we can somehow find the number of 1s in each consecutive series of 1s
        #then for each series, number of substrings would be n * (n+1) // 2
        
        #Case 1 : If the given string contains only 0s
        if len(set(s)) == 1 and "0" in s:
            return 0
        
        #Case 2 : If the given string contains only 1s
        if len(set(s)) == 1 and "1" in s:
            n = len(s)
            answer = (n * (n+1))//2
            return answer
        
        #Case 3 : If the given string contains both 0s and 1s
        #See the given example : "0110111"
        #Taking sum of digits, we can write it as : "0120123" (taking 0 when we encounter a 0)
        #Now, summing this up, we will have 1 + 2 + 1 + 2 + 3 = 9, which is our answer
        
        result = 0 
        current_sum = 0 
        
        for digit in s:
            if digit == '0':
                current_sum = 0
            else:
                current_sum += 1 
                result += current_sum
                
        return result % (10**9+7)
        