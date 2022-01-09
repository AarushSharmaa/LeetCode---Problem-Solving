# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        #p and q are roots of tree1 and tree2 respectively 
        
        
        #edge case : if both of them are null, we will return True
        if p == None and q == None:
            return True
        
        #edge case : if one of the roots is null and other is not, we will return False 
        if p == None or q == None:
            return False
        
        #edge case : if roots are having different values, we will return False
        if p.val != q.val:
            return False 
        
        #now, we will check if left and right subtrees of both are trees are equivalent or diffferent 
        
        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)
        if left_check == True and right_check == True:
            return True