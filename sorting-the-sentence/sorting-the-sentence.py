class Solution:
    def sortSentence(self, s: str) -> str:
        
        #let us take first test case in comments
        words = s.split() #array of strings
        ans = []
        
        for i in words:
            ans.append(i[len(i) - 1])
            
        ans.sort() #this ans contains order of integers in the form of strings eg. "1", "2", "3", "4"...
        answer = "" 
        
        for i in ans:
            for j in words:
                if i in j: #if a particular digit is in the array of words
                    answer +=  j + " " 
                    break
        #answer will now be "This1 is2 a3 sentence4"
        s1 = answer.split() #s1 = ["This1", "is2", "a3", "sentence4"]
        #print(s1)
        output = "" #this will hold our final answer
        for i in range(0, len(s1)):
          
            for j in range(0, len(s1[i]) - 1):
                output += s1[i][j]
                
            #EXCEPT the last character, we will add a space after every word
            #the last character will be at len(s) - 1 position
            #so, below condition comes in picture
            if i != len(s1) - 1: 
                output += " "
            
        return output
