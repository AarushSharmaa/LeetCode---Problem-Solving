# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        #if we have an empty tree or have reached a node that is null
        if root == None:
            return 0 
        
        #first, we will calculate the number of nodes of the left subtree
        nodes_left_subtree = self.countNodes(root.left)
        
        #second, we will calculate the number of nodes of the right subtree
        nodes_right_subtree = self.countNodes(root.right)
        
        answer =  1 + nodes_left_subtree + nodes_right_subtree
    
        return answer
        