# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        #here, we dont have access to head
        #but we have access to the node we are supposed to delete - it is definitely not a tail node
        #WHY DON'T WE HAVE ACCESS TO HEAD
        
        node.val = node.next.val #at the value place of node, we are changing it and assigning it the value of the next node
        node.next = node.next.next #then, now that we have changed node to next node, we can simply change next of node 
        
        #this way, we have changed the value of node, keeping the memory address. I guess it may lead to some complications
        
        
        