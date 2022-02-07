class Solution:
    def frequencySort(self, s: str) -> str:
        
        
        #REQUIREMENT : sort in decreasing order on the basis of frequency of characters and combine them 
        
        #an extra string to hold the output
        answer = ""
        
        #creating a dictionary where each element corresponds to its frequencty - O(N) Time
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        #another array to store just the occurences in descending form - O(N) Time
        occurence = []
        for value in freq.values():
            occurence.append(value)
            
        occurence.sort(reverse = True)
        
        #now the final step to find out elements corresponding to frequency of them in descending form
        #O(N) Time as lookup in dictionary is O(1) Time only
        for f in occurence:
            for key in freq:
                if freq[key] == f and key not in answer:
                    answer += (f * key)
        return answer
    
        #Time Complexity : O(N) + O(N) + O(N) = O(N)
        #Space Complexity : O(N) due to extra dictionary and array declared
                    
                
        
            