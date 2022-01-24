class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        #O(N^2*log(N^2)) Time and O(1) Space
        
        array = []
        for arrays in matrix:
            for element in arrays:
                array.append(element)
        
        array.sort()
        return array[k-1]