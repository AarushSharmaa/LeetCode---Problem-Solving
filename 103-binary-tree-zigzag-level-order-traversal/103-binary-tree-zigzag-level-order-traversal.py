# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return root
        
        array = []
        queue = []
        level = 0
        queue.append(root)
        
        while len(queue) > 0:
            
            subarray = [] #will behave as a stack if the level is odd
            size = len(queue)
            
            for i in range(0, size):
                node = queue.pop(0) #pops the front element of the queue and stores in it variable named *node*
                
                subarray.append(node.val)
                

                if node.left != None:
                    queue.append(node.left)
                
                if node.right != None:
                    queue.append(node.right)
            
            #now, if the level was odd, we will first reverse the subarray as it was behaving like a stack
            if level % 2 != 0:
                subarray.reverse()
            
            array.append(subarray)
            
            level += 1 
            
        return array
        