class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        nums1.extend(nums2) #this is now the merged array
        nums1.sort()
        size = len(nums1)
        if size % 2 != 0:
            mid = size // 2 
            return float(nums1[mid])
        else:
            mid = size // 2 
            return (nums1[mid] + nums1[mid-1]) / 2