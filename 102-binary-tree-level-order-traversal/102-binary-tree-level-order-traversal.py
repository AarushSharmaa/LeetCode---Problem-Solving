# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        
        if root == None: # if root is None, there is no deeper level to go to. Then, return [] which is the root. 
            return root
        
        array = [] #this will return level order traversal in the form of subarrays of each level 
        queue = [] #this will traverse the tree - follows FIFO
        queue.append(root) 
        
        while len(queue) > 0:
            
            subarray = []
            size = len(queue)
            
            for i in range(0, size):
                
                node = queue.pop(0) 
                subarray.append(node.val)
                
                if node.left != None: 
                    queue.append(node.left)
                    
                if node.right != None: 
                    queue.append(node.right)
                    
            array.append(subarray)
            
        return array