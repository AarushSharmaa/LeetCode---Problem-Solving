# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        
        #APPROACH :
        
        #remove all the nodes of the linkedlist that has node.val = val 
        #here, val in node.val represents the data part of the node
        #and the other node represents an integer given in the question
        #return the head of the modified linkedlist
        
        #Let us now handle a few edge cases
        
        while head != None and head.val == val:
            head = head.next
            
        #In all other cases where size of LinkedList > 1
        current = head
        while current != None:
            if current.next != None and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head