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
        #other loop is to traverse and reach (size - n)th node -- as parent of the node we are trying to delete 
        #will be present at (size - n)th node
        
        #first loop - to determine size of the given LinkedList
        temp = head
        size = 0
        
        while temp != None:
            size += 1
            temp = temp.next 
        
        #case 2 : if n == size of linkedlist, we will need to delete the head
        #so we will simply change our head
        if n == size:
            head = head.next
            return head
        
        #second loop - to traverse and reach the parent node of nth node from end  
        c = 1
        temp = head
        while c < (size - n):
            c += 1
            temp = temp.next
        
        #now temp will represent the parent of the node we have to delete
        store = temp.next.next
        temp.next = store
        return head
        
        
        #Lets try do it in 1 loop or a 1 pass algorithm as above was a 2 pass algorithm
        
        #now, we can use 2 pointers separated by n units initially. So that, when the one pointer reaches tail, 
        #first pointer will be at the parent at the node which we want to delete : or the nth node from the end
        
        
        
        
        
        
        
            
            