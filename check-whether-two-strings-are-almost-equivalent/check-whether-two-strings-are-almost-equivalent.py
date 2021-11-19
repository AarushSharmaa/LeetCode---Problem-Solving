class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        d1 = {} #will hold elements and their frequencies of word1
        d2 = {} #will hold elements and their frequencies of word2
        
        #let us populate d1 now
        for element in word1:
            if element in d1:
                d1[element] += 1
            else:
                d1[element] = 1
            
        #let us populate d2 now
        for element in word2:
            if element in d2:
                d2[element] += 1
            else:
                d2[element] = 1
        
        #let us implement our core logic now
        frequency = [] #this will hold difference of frequencies of characters occuring in both words
        
        #First, we will cover frequencies of elements that are in both word1 and word2 and then
        #we will cover frequencies of those elements that are just in word1
        
        for element in d1:
            if element in d2:
                difference = d2[element] - d1[element]
                #now, we want to take only positive differences
                if difference < 0:
                    frequency.append(-1 * difference)
                else:
                    frequency.append(difference)
            else: #element not in d2
                difference = d1[element]
                frequency.append(difference)
        
        #now let us cover elements in d2 that are not in d1
        for element in d2:
            if element not in d1:
                difference = d2[element]
                frequency.append(difference)
                    
        maxm = max(frequency)
        #if the frequency's maximum value is less than 4, that means result will be True
        if maxm < 4:
            return True
        else:
            return False
            
        