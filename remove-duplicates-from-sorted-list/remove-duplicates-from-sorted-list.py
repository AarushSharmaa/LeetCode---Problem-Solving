# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Approach : We can initialise a current to head and then inside a while loop
        #keep traversing to check if the current node == next node : if it is, we change its link
        #else, we keep traversing the linkedlist in forward direction
        
        #Complexity Analysis : O(N) Time and O(1) Space
        
        #if the Linkedlist is empty or is of size 1
        while head == None or head.next == None:
            return head
        
        #in all the other sizes of LinkedList
        current = head
        while current != None and current.next != None: #while current != None
            temp = current.next 
            
            if current.val == temp.val:
                current.next = current.next.next
            else:
                current = current.next
        return head