class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
        heap=[]
        
        #we will create a heap with these three parameters : sum, i, j
        for i in range(0, len(nums1)):
            heapq.heappush(heap,(nums1[i]+nums2[0], i, 0)) 
        
        final=[]
        count = 0
        
        while(heap and count < k):
            
            sums, i, j = heapq.heappop(heap)
            
            final.append([nums1[i], nums2[j]])
            if(j + 1 < len(nums2)):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            count += 1
        
        return final
            
        