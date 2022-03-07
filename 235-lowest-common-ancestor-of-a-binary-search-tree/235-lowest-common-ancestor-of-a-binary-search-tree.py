# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        if root == None:
            return None
        
        if (root.val == p.val  or root.val == q.val):
            return root
        
        maxm = max(p.val, q.val)
        minm = min(p.val, q.val)
        
        if minm < root.val < maxm:
            return root 
        
        if root.val > minm and root.val > maxm:
            return self.lowestCommonAncestor(root.left, p, q)
            
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
        
        
        
        