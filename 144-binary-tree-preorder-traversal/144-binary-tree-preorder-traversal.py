# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #Root.VALUE --> LST --> RST
    
    def traversal(self, root, preorder):
        
        if root == None:
            return
    
        preorder.append(root.val)
        self.traversal(root.left, preorder)
        self.traversal(root.right, preorder)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        self.traversal(root, preorder)
        return preorder
        
        
        