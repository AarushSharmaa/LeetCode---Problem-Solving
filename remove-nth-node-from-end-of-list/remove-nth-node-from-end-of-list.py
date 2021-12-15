# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #to remove nth node from the end of the linkedlist, we will have to reach its parent node
        #parent of nth node from the end is (size - n)th node away from the beginning of the linkedlist
        #we can traverse till this point and change the links to achieve desired results
        #we can know that 1 <= n <= size as given in Constraints
        
        #case 1: if linkedlist is empty or is of size 1, we will delete the head 
        if head == None or head.next == None:
            return 
        #all other cases
        
        #first loop to determine the size of linkedlist
        #other to traverse and reach (size - n)th node
        
        #first loop - to determine size
        temp = head
        size = 0
        
        while temp:
            size += 1
            temp = temp.next 
        
        #case 2 : if n == size of linkedlist, we will need to delete the head
        if n == size:
            head = head.next
            return head
        
        #second loop - to traverse and reach the parent node of nth node from end  
        c = 1
        temp = head
        while c < (size - n):
            c += 1
            temp = temp.next
        
        store = temp.next.next
        temp.next = store
        return head
        
        
        
            
            