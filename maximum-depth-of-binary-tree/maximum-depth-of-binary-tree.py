# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #if we have an empty tree or if we have reached the leaf nodes
        if root == None:
            return 0 
        
        #first, let us calculate the height of left subtree
        lh = self.maxDepth(root.left)
        
        #then, we can make a call to right subtree and get its height 
        rh = self.maxDepth(root.right)

        #and then, we can calculate the maximum of height of left and right subtree and add 1 (contribution of root) to it
        #this way, we will get of entire binary tree
        answer = 1 + max(lh, rh)
        
        return answer