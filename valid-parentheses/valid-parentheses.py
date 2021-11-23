class Solution:
    def isValid(self, s: str) -> bool:
        
        
        #as long as length of s is 0, we will run the loop
        #and convert all brackets type with an empty string
        """
        
        while len(s) > 0:
            l = len(s)
            
            #below condition will only run for cases when there are legal brackets
            #if there are no legal brackets, below statement will simply not replace anything 
            #and if it does not replace anything, length will remain same as that of original string
            #that means, it is an invalid sequence of brackets
            
            s = s.replace('()','').replace('{}','').replace('[]','')
            if l == len(s):
                return False
        return True
        """
        
        #if there are only 1 type of bracket () -- below code works
        
        """
        stack = []
        n = len(s)
        for i in range(0, n):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
        """
        
        stack = []
        n = len(s)
        for i in range(0, n):
            
            #first, we will cover the () bracket 
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) == 0:
                    return False
                else:
                    if stack[len(stack) - 1] == "(":
                        stack.pop()
                    else:
                        return False
            
            #now, we will try to eliminate the [] bracket
            if s[i] == "[":
                stack.append(s[i])
            elif s[i] == "]":
                if len(stack) == 0:
                    return False
                else:
                    if stack[len(stack) - 1] == "[":
                        stack.pop()
                    else:
                        return False
            
            #now, wei will try to eliminate the {} bracket
            if s[i] == "{":
                stack.append(s[i])
            elif s[i] == "}":
                if len(stack) == 0:
                    return False
                else:
                    if stack[len(stack) - 1] == "{":
                        stack.pop()
                    else:
                        return False
        
        #at the end, if the stack is empty, means all opening got a closing 
        #so it is a valid sequence and we will return True
        if len(stack) == 0:
            return True
        #else, we will return False
        else:
            return False

        
        