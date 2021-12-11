class Solution:
    def countHomogenous(self, s: str) -> int:
        
        #return the number of homogenuos substrings of s
        #a string is homogenous if all the characters of the string are the same
        
        #Brute Force Approach : 
        #Traverse over each substring and as soon as we find a homogenous substring
        #increment our answer, which we can initialise in the beginning
        #Complexity Analysis : O(N^2) Time and O(N) Space 
        
        #Clears 77/84 Test Cases and then throws TLE
        
        """
        n = len(s)
        answer = 0 
    
        for i in range(0, n):
            substring = ""
            for j in range(i, n):
                
                substring += s[j]
                
                if len(set(substring)) == 1:
                    answer += 1
                else:
                    break
        return answer
        """
        
        #Lets try to better our time now --  Taking help from Discussion Section
        #IMPORTANT OBSERVATION TO NOTICE : if there is a string with aaaaa (5 a's), number of homogenous substrings will be
        #(5 * (5 + 1)) / 2
        #So, Our task now is to find strings with maximum length where elements are equal
        
        n = len(s)
        p = 1 #this will indicate the number of consecutive strings
        result = 0 #this wil count the number of homogenous substrings forming out of them
        for i in range(0, n - 1):
            #if the current string == next string, we will increase the p
            if s[i] == s[i + 1]:
                p += 1
            #if the current string != next string, that means we have seen all consecutive 
            #strings being considered of the current string
            #and we will calculate the number of homogenous substrings out of them 
            else:
                result = result + p * (p + 1) / 2
                p = 1
        
        #At the end, for the string at (n-1)th index :
        result = result +  p * (p + 1) / 2
        return int(result % (10**9 + 7))
        