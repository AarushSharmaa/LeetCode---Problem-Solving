class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        import heapq 
        heapq.heapify(nums)
        array = heapq.nlargest(k, nums)
        return array[k-1]
        
        #now, our given nums is converted 
        