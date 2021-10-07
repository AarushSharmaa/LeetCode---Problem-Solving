class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        index = 0
        temp = s.copy() 
        for i in range(n - 1, -1, -1):
            s[index] = temp[i]
            index += 1
        return s
        
        
            
        