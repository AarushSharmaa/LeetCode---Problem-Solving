class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        #return true if ransomNote can be constructed from magazine and false otherwise
        
        d1 = {} #will store elements and frequencies of ransomNote
        d2 = {} #will store elements and frequencies of magazine
        
        for i in ransomNote:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        for i in magazine:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
                
        
        #now we can check if a key exists in d1, if its frequency <= corresponding frequency in d2
        #then, True. Else, return False even if one of the keys do not fulfil the condition
        
        count = 0 #ideally, if it becomes == len(d1), it means all keys fulfil the condition required
        for key in d1:
            if key in d2:
                if d1[key] <= d2[key]:
                    count += 1
            else: #if a key present in d1 is not in d2, we will never be able to form words of ransomNote
                return False
            
        if count == len(d1):
            return True