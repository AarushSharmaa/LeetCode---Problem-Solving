class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return list((zip(*collections.Counter(nums).most_common(k))))[0]
    
        #  Counter -  to extract the top k frequent elements
        # most_common(k) return a list of tuples, where the first item of the tuple is the element,
        # and the second item of the tuple is the count
        # Thus, the built-in zip function could be used to extract the first item from the tuples
        
        #APPROACH 2
        
        #We will use a heap 
        
        import heapq
        heapq.heapify(nums) #we have converted given input to min heap 
        return heapq.nlargest(k, nums)
        
        
        
        
        