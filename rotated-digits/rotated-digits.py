class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        #Note : The range in the given question is inclusive
        
        #Requirement of the question : 
        #We need to find number of **good integers** and return it
        #An integer is good if after rotating each digit individually by 180 degrees, we get a valid number different from original number
        
        #Rules of Rotation : 
        #0, 1, and 8 rotate to themselves. 
        #2 and 5 rotate to each other
        #6 and 9 rotate to each other
        #rest of the numbers do not rotate to any other number and become invalid 
        
        #Observation - 0, 1 and 8 do not matter
        #2, 5, 6, 9 aaya kisi number mai to its a good number
        #3, 4, 7 - ye invalid hai
    
        #Complexity - O(N^2) Time in the worst case and O(1) Space
        
        count = 0
        
        for i in range(1, n + 1):
            string = str(i)
            
            #3, 4 and 7 - they are rest of the numbers that become invalid - so we must handle them
            if '3' in string or '4' in string or '7' in string:
                continue
                
            #now, we just want to see if the string contains any valid number or not
            #if it does, increment counter by 1
            if '2' in string or '5' in string or '6' in string or '9' in string:
                count += 1
                
        return count