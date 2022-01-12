# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #LST --> Root.Value --> RST 
    
    
    def traversal(self, root, preorder):
        if root != None:
            self.traversal(root.left, preorder)
            preorder.append(root.val)
            self.traversal(root.right, preorder)
        
            
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        self.traversal(root, preorder)
        return preorder
        
        