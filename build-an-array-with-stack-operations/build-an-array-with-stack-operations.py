class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        #list will contain integers from 1 to n inclusive -- here, n is given
        
        #Let us observe properties of Stack very carefully
        
        array = [] #this is the list which will contain elements from 1 to n (inclusive of both) 
        for i in range(1, n+1):
            array.append(i) 
        
        answer = [] #this will hold our output
        #push for numbers that are in target
        #push and then pop for numbers that are not in target
        
        n = len(target)
        
        stack = []
        
        for element in array:
            
            if element in target: #it means that target already has the element covered
                #we simply need to push it
                answer.append("Push")
                stack.append(element)
                
            else: #it means that target does not have the element covered
                #so, first we will push it, then pop it 
                answer.append("Push")
                answer.append("Pop")
                stack.append(element)
                stack.pop()
            
            #if our stack produces desired target array, we will stop and break out of the loop
            if stack == target:
                break
            
        return answer