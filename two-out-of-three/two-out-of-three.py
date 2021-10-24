class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        #return a distinct array containing all the values 
        #that are present in at least two out of the three arrays.
        
        #NOTE - values can be in any order
        
        d1 = {} #will hold the elements and its frequencies of nums1 
        d2 = {} #will hold the elements and its frequences of nums2
        d3 = {} #will hold the elements and its frequences of nums3
        
        #populating d1 with elements of nums1
        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        #populating d2 with elements of nums2
        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        
        #populating d3 with elements of nums3
        for i in nums3:
            if i in d3:
                d3[i] += 1
            else:
                d3[i] = 1
            
        output = [] #this will hold our output
        
        #Core Logic comes here now -->
        
        #We can iterate over the largest dictionaries and check if the element is present in atleast 1 other
        #dictionary or not. If it is, we add it to our output.
        
        
        for element in d1:
            if element in d2 or element in d3:
                output.append(element)
                
        for element in d2:
            if element in d1 or element in d3:
                output.append(element)
                
        for element in d3:
            if element in d2 or element in d1:
                output.append(element)
                
        answer = set(output)
        return list(answer)
        
        
        