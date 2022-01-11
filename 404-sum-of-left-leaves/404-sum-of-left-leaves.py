# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        #basically, we have to return the sum of values present at left leaves only 
        #if there is just one node or if we reached the tails of the tree
        
        #---------below code counts the number of leaves---------------
        
        """
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        l1 = self.sumOfLeftLeaves(root.left)
        l2 = self.sumOfLeftLeaves(root.right)
        
        answer = l1 + l2
        
        return answer
        """
        
        if root == None:
            return 0

        # does this node have a left child which is a leaf?
        if root.left != None and root.left.left == None and root.left.right == None:
			# gotcha
            return (root.left.val + self.sumOfLeftLeaves(root.right))

        # no it does not have a left child or it's not a leaf
        else:
			# bummer
            
            h1 = self.sumOfLeftLeaves(root.left)
            h2 = self.sumOfLeftLeaves(root.right)
            return h1 + h2
        