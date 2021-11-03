class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        #let us dry run Example 1 
        
        d1 = {} #will hold elements of list1 corresponding to its index
        d2 = {} #will hold elements of list2 corresponding to its index
        
        #populating d1 with elements of list1 corresponding to its indices
        for i in range(0, len(list1)):
            d1[list1[i]] = i
        #d1 = {"Shogun" : 0, "Tapioca Express" : 1, "Burger King" : 2, "KFC" : 3}
        
        #populating d2 with elements of list2 corresponding to its indices
        for i in range(0, len(list2)):
            d2[list2[i]] = i 
        #d2 = {"Piatti : 0, "The Grill at Torrey Pines" : 1, "Hungry Hunter Steakhouse" : 2, "Shogun" : 3}

        d3 = {} #will hold common elements in both lists corresponding to the sum of their indices 
        
        #populating d3 with common elements correspnding to their sum of indices
        for element in d1:
            if element in d2:
                d3[element] = d1[element] + d2[element]
        #d3 = {"Shogun" : 3}
                
        output = [] #will hold our final answer
        ans = [] #will hold all the sumn of indices and then we can find minimum of them
        
        #Case 1 : If there is only 1 common element
        #we can simply add it to our output
        if len(d3) == 1: 
            for element in d3:
                output.append(element)
            return output
        
        #Case 2 : If there are multiple common elements
        #we will have to find elements with minimum sum of their indices
        else:
            for value in d3.values():
                ans.append(value) 
                
            minm = min(ans)
            for element in d3:
                if d3[element] == minm:
                    output.append(element)
            return output

            
        
        