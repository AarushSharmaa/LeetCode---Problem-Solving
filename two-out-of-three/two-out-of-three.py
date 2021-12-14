class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        d1 = {} #dictionary1
        d2 = {} #dictionary2
        d3 = {} #dictionary3
        
        #populating d1 with elements of nums1 - O(N) Time
        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        #populating d2 with elements of nums2 - O(N) Time
        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        
        #populating d3 with elements of nums3 - O(N) Time
        for i in nums3:
            if i in d3:
                d3[i] += 1
            else:
                d3[i] = 1
        
        output = [] #will hold our output
        
        #O(N) Time as lookups in a dictionary will costs only O(1)
        for element in d1:
            if element in d2 or element in d3:
                output.append(element)
        
        #O(N) Time 
        for element in d2:
            if element in d1 or element in d3:
                output.append(element)
        
        #O(N) Time
        for element in d3:
            if element in d1 or element in d2:
                output.append(element)
        
        #to remove duplicates, we have used set
        #so, this will consume O(N) Time
        return list(set(output))
    
        #Overall Time Complexity - O(N)
        #Overall Space Complexity - O(N)