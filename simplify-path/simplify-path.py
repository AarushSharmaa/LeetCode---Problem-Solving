class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        
        #"." refers to the current directory -- just skip it
        #".." refers to the directory up a level
        #// are treated as single slash 
        array = path.split("/")
        
        for element in array:
            
            if element == "." or element == "": #it means we are in the current directory 
                #no need to keep it in our simplified path
                continue 
                
            elif element == "..": #it means we are in an higher level directory
                #and we need to come down 
                if len(stack) != 0: #if the stack is not empty 
                    stack.pop()
            else:
                stack.append(element)
                
        if len(stack) == 0:
            return "/"
        
        elif len(stack) == 1:
            return "/" + stack[0]
        
        else:
            answer = ""
            for i in stack:
                answer += "/" + i
            return answer
                
        