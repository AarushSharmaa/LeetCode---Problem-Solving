# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        #let us do an inorder traversal and store all the nodes of the tree in an array
        #if the array is sorted, we can conclude that given BT is a BST
        array = []
        self.inorder(root, array)
        count = 1
        for index in range(1, len(array)):
            if array[index] > array[index-1]:
                count += 1
        if count == len(array):
            return True
        
        
    def inorder(self, root, array):
        
        
        if root == None:
            return 
        
        self.inorder(root.left, array)
        array.append(root.val)
        self.inorder(root.right, array)
        