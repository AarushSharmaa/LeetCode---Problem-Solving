class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        #ops[i] is the ith operation we must apply to the record
        
        #this problem involves adding and deleting elements at each step -- so we think in terms of using stack
        
        stack = []
        
        for element in ops:
            
            
            if element == "C":
                stack.pop()
            
            elif element == "D":
                stack.append(2 * stack[len(stack)-1])
            
            elif element == "+":
                stack.append(stack[len(stack) - 1] + stack[len(stack) - 2])
            
            else:
                stack.append(int(element))
        
        answer = 0 
        for index in range(len(stack) - 1, -1, -1):
            answer += stack[index]
        return answer
                