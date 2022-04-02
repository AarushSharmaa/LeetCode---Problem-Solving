class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        #APPROACH 1: O(N^2*log(N^2)) Time and O(N) Space
        
        """
        array = []
        for arrays in matrix:
            for element in arrays:
                array.append(element)
        
        array.sort()
        return array[k-1]
        """
        
        #APPROACH 2: Let us try to optimise this by using some deductions 
        #BINARY SEARCH ON ANSWER
        
        
        
        
        #APPROACH 3: Heaps Approach 
        import heapq
    
        heap = []
        
        for i in range(0, len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
            count = 0
            
        while (heap and count < k):
            answer, i1, j1 = heapq.heappop(heap)
            if (j1 + 1) < len(matrix):
                heapq.heappush(heap, (matrix[i1][j1 + 1], i1, j1 + 1))
            count += 1
                
        return answer


        
        
        
        
    