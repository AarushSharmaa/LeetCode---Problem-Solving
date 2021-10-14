class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        #Brute Force -- Just check for all the pairs
        #Time Consumed - O(N^2) and Space Cosumed - O(1)\
        
        """
        n = len(arr)
        for i in range(0, n):
            for j in range(0, n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        """
        
        #Lets try it in less time -- We can use a HashMap in Python to do it in O(N) Time and O(N) Space
        
        n = len(arr)
        d = {}
        for i in range(0, n):
                d[2 * arr[i]] = i 
                
        for j in range(0, n):
            if arr[j] in d:
               if j != d[arr[j]]:
                    return True
        return False

        