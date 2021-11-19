class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        #return the number of vowel substring
        #let us consider all possible substrings one by one
        #and as soon as we have any combination of vowels, we will increment our answer
        
        #O(N^2) Time and O(1) Space
        
        vowels = ["a", "e", "i", "o", "u"]

        
        answer = 0
        n = len(word)
        for i in range(0, n):
            substring = ""
            for j in range(i, n):
                substring += word[j]
                if set(substring) == set(vowels):
                    answer += 1
        return answer
        