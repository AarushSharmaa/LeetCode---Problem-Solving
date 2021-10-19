class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        
        alphabets = {"a": ".-",
                     "b" : "-...",
                     "c" : "-.-.",
                     "d" : "-..",
                     "e" : ".",
                     "f" : "..-.",
                     "g" : "--.",
                     "h" : "....",
                     "i" : "..",
                     "j" : ".---",
                     "k" : "-.-",
                     "l" : ".-..",
                     "m" : "--",
                     "n" : "-.",
                     "o" : "---",
                     "p" : ".--.",
                     "q" : "--.-",
                     "r": ".-.",
                     "s" : "...",
                     "t": "-",
                     "u" : "..-",
                     "v" : "...-",
                     "w" : ".--",
                     "x" : "-..-",
                     "y" : "-.--",
                     "z" : "--.."}
        
        
        #return the number of different transformations among all words we have
        mat = []
        for i in words:
            transformation = ""
            for j in i:
                transformation += alphabets[j]
            if transformation not in mat:
                mat.append(transformation)
        return len(mat)
                
        
                
                