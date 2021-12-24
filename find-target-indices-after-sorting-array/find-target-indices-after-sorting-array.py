class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        #Approach : 
        
        #first, we need to sort the given array is ascending form
        #then, we need to return the list of indices where this target element is present in the given array
        #if there are no target indices, return an empty list 
        
        #O(N*log(N)) Time and O(N) Space
        
        nums.sort()
        n = len(nums)
        output = []
        for index in range(0, n):
            if nums[index] == target:
                output.append(index)
        return output