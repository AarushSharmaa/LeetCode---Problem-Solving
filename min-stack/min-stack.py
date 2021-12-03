#It has been mentioned inside Constraints that the stack underflow conditions will be taken care of
#so we don't need to worry about it in our code

class MinStack:

    def __init__(self):
        self.stack = []
        
    #This function will add an element to the top of the stack and return it
    #Below code takes O(1) Time as we are simply adding an element to the top and no traversal over the stack is required
    def push(self, val: int) -> None:
        element_added = self.stack.append(val)
        return element_added
    
    #This function will remove the element from the top of the stack and return it
    #Below code takes O(1) Time as we are simply removing an element from the top and no traversal over the stack is required
    def pop(self) -> None:
        element_removed = self.stack.pop()
        return element_removed
        
    #This function returns the top element of the stack
    #Below code takes O(1) Time as we are accessing the top element of the stack directly
    #and no traversal over the stack is required
    def top(self) -> int:
        top_element = self.stack[-1]
        return top_element
        
    #This function retrieves the minimum element in the stack
    #Below code takes O(N) Time as we will have to traverse over the entire stack to figure out the minimum
    def getMin(self) -> int:
        minm = min(self.stack)
        return minm
    
    #Lets try to do it in constant - O(1) Time
    
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()