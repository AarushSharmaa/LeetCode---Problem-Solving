# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #first, we will count total number of nodes
        #second, we will do n//2 traversals to reach the middle node
        
        #calculation of total number of nodes
        count = 0 
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        #we will do n//2 traversals to reach the middle node and then return it
        temp = head
        c = 0
        while c < count // 2:
            temp = temp.next
            c += 1
            
        return temp
        
        
        