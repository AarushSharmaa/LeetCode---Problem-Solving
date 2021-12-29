class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        #Return the kth distinct string present in arr
        #If there are less than k distinct strings, return an empty string ""
        
        #Approach :
        #We will be using an ordered dictionary as it maintains relative ordering of elements
        #After populating this with elements and their frequency, we will declare a counter variable named "count"
        #This will keep a count of all distinct strings(elements whose frequency is 1)
        
        #Let us declare an Ordered Dictionary now
        from collections import OrderedDict
        od = OrderedDict() #Here, we have an ordered dictionary 
        
        #Let us populate our dictionary now
        #We are aiming to create a dictionary with elements as keys and their frequencies as values
        for i in arr:
            if i in od:
                od[i] += 1
            else:
                od[i] = 1 
        
        #Now, we will declare a variable named count which will keep track of number of distinct integers
        count = 0 
        for element in od:
            #if od[element] == 1 : it means it is disinct
            #count variable will keep a count of distinct strings present in the given array
            if od[element] == 1:
                count += 1
                if count == k:
                    return element
                
        #if we do not get any answer from the above loop
        #it means that there is no kth distinct string present in the given array
        #so, we will return an empty string
        else:
            return ""