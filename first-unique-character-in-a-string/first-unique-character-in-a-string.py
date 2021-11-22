class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        #find first non-repeating character and return its index
        #if it does not exists, return -1 
        
        #Brute Force Solution - We can fix one character and then iterate over the remaining string
        #If the character is found again, we will simply break out of the loop and if not
        #Then, we will return the index and it will be our answer
        #O(N^2) Time and O(1) Space
        
        n = len(s)
        
        for i in range(0, n):
            for j in range(0, n):
                
                #here is our core logic, where i != j and if we found any character getting repeated
                #we will break out of the loop 
                #if no such repitition is found, we will return its index after this loop is completed 
                #as shown below the else statement
                if (i != j) and (s[j] == s[i]):
                    break
            else:
                return i
        
        #if no such character is found, return -1
        return -1
    
            
        
        #Optimal Solution Approach - We will use a hashtable to store elements and their frequency 
        #Then, we will iterate over the dictionary and find elements whose frequency is 1 and return its
        #corresponding index from the given string
        
        
        #O(N) Time and O(N) Space
        
        """
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    
        for i in d:
            if d[i] == 1:
                return s.index(i)
        else:
            return -1
        """