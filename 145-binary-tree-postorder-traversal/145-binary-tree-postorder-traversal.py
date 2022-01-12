# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #LST --> RST --> Root.Value
    
    def traversal(self, root, preorder):
        if root == None:
            return 
        self.traversal(root.left, preorder)
        self.traversal(root.right, preorder)
        preorder.append(root.val)
    
    
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        self.traversal(root, preorder)
        return preorder