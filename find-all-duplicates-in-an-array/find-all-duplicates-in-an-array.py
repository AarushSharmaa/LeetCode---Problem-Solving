class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        #return an array of all integeres that appears twice
        #nums is in the range of [1,n] inclusive
        
             
        from collections import Counter
        c = Counter(nums)
        temp = nums.copy()
        for i in temp:
            nums.remove(i)
        for i in c:
            if c[i] == 2:
                nums.append(i)
        return nums
        
        