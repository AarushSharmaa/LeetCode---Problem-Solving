class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        #O(N) TIME AND O(N) SPACE
        
        """
        dictionary = {} #this will hold elements corresponding to its frequency in the hashtable
        
        for i in s:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        
        frequency_array = [] #will hold frequency of all different elements
        
        for values in dictionary.values():
            frequency_array.append(values)
        
        #if we ensure to remove all duplicates using set and find that length == 1
        #it means all the present frequencies in the frequency array must have been same, so return True
        if len(set(frequency_array)) == 1:
            return True
        else:
            return False
        """
        
        #Let us experiment with a more basic thought process
        #O(N^2) TIME AND O(N) SPACE
        
        s1 = list(set(s))
        n1 = len(s1)
        n = len(s)
        output = []
        
        for i in range(0, n1):
            count = 0 
            for j in range(0, n):
                if s1[i] == s[j]:
                    count += 1 
            output.append(count)
            
        if len(set(output)) == 1:
            return True
        else:
            return False
        
        
        