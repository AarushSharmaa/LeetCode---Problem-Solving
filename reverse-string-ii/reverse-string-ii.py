class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        n = len(s)
        
        if n < k: #reverse s entirely
            return s[::-1]
        
        elif k <= n <= (2*k): #just reverse the first k characters
            answer = ""
            
            for i in range(k - 1, -1, -1): #reversing the first k characters
                answer += s[i]
                
            for i in range(k, n): #adding the remaining portion to our answer
                answer += s[i]
                
            return answer
        
        else: #reverse the first k characters for every 2k characters counting from the start of the string
            answer = ""
            for i in range(0, n, 2 * k):
                answer += s[i : i + k][::-1]  + s[i + k: i + k + k]
            return answer
                