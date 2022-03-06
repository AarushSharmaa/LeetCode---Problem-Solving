# Definition for a binary tree node.


#In this problem, we have to convert a given array(sorted form) to a BST
#We can choose any of the element from this array as root - suppose its index is i 
#then, LST will have values of elements present between indexes (0, i-1) and
#RST will have values of elements present between (i+1, len(nums)-1)

#Now, we want a height balanced output, so we will choose middle index element as root 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
                  
            self.val = val
            self.left = left
            self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        i = 0 
        j = len(nums) - 1
        value = self.makeBST(nums, i, j) 
        return value
        
        
    def makeBST(self, nums, i, j):
        
        #our termination condition 
        if i > j:
            return 
        
        mid = (i + j)//2
        root = TreeNode(nums[mid], None, None)
        
        root.left = self.makeBST(nums, i, mid-1)
        root.right = self.makeBST(nums, mid+1, j)
        
        return root
        
