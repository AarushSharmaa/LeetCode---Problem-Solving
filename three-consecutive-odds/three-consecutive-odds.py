class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        
        n = len(arr)
        
        #if length of the array is less than 3, we will never have 3 consecutive odd numbers
        if n < 3:
            return False
        
        for i in range(0, n-2):
            #if a given number is odd
            #we will check the following two numbers
            if arr[i] % 2 != 0 :
                if arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                    return True 
            
            #if a given number is even
            #we will continue our iterations
            else:
                continue 