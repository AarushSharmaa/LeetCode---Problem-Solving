# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # A few important things to remember about Object Oriented Programming : From Python's Perspective
    #   {
    
    #Observe how functions are defined separately inside classes.
    #The self parameter is a reference to the current instance/object of the class,
    #and is used to access variables that belongs to the class.
    
    #for any function in the class, first parameter has to be self always
    #   }
    
    
    #Time - O(N) and Space - O(N) due to internal call stack
    
    def inorder(self, root, array):
        
            if root == None:
                return 
            
            self.inorder(root.left, array)
            array.append(root.val)
            self.inorder(root.right, array)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #we will do an inorder traversal of the tree and keep storing nodes in a separate array
        #then, this array will contain sorted form of nodes, and we can return (k-1)th index from the array
        
        array = []
        self.inorder(root, array)
        return array[k-1]
        