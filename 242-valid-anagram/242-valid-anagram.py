class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #TRUE : if t is an anagram of s
        #anagram - if t is formed from the same combination of letters in s : where each letter are used exactly once
        
        
        #O(N) Time and O(N) Space
        
        if len(s) != len(t):
            return False
        
        
        d1 = {} #will contain frequency of characters of string s
        d2 = {} #will contain frequency of characters of string t 
        
        #populating d1 
        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        
        #populating d2
        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1
        
        #comparing dictionaries which contain character and its frequency of both strings  
        if d1 == d2:
            return True