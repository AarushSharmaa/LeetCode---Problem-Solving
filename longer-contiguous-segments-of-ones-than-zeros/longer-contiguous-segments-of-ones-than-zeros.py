class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        #If longest consecutive segment of 1's is strictly longer than longest consecutive segment of 0's
        #return True
        
        #Complexty Analysis - O(N) Time and O(1) Space
        
        count_of_ones = 0 #count of contiguous 1's
        count_of_zeroes = 0 #count of contiguous 0's
        a1 = 0 #will count maximum number of contiguous 1's
        a2 = 0 #will count maximum number of contiguous 0's
        
        for i in s:
            if i == "1":
                count_of_ones += 1
                count_of_zeroes = 0 
            else:
                count_of_zeroes += 1 
                count_of_ones = 0
            
            a1 = max(a1, count_of_ones)
            a2 = max(a2, count_of_zeroes)
            
        if a1 > a2:
            return True
        else:
            return False
            
            
        