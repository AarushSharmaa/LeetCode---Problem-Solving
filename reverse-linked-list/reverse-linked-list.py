# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Iterative method  
        
        #if you will return head of the reversed linkedlist, you will return the
        #output in the desired form 
        
        #Instead of swapping elements like we would have in an array, here, we would be changing links of the 
        #nodes. This way, we would be reversing the linkedlist without tampering with the data part of the nodes.
        #Tampering with data part of nodes may lead to complications. 
        #O(N) Time and O(1) Space
        
        current = head
        previous = None
        
        while current != None: #it means current != Null

            temp = current.next
            current.next = previous 
            previous = current
            current = temp 
            
        return previous
            
            