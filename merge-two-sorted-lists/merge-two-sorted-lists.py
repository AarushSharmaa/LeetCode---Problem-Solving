# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Approach 1 
        #Complexity Analysis : O(M + N) Time and O(M + N) Space
        
        #Create a separate LinkedList and using two pointers p1 and p2 which points to heads of L1 and L2 initially,
        #keep comparing values of L1 and L2 
        #and keep adding them in our separate LinkedList. The termination condition would be when p1 or p2 points to Null
        #Once this happens, we can directly add the remaining linkedlist to our output linkedlist
        
        
        
        #Approach 2
        #Complexity Analysis : O(M + N) Time and O(1) Space
        
        #first, we will determine the overall head of the merged linkedlist
        #and the tail of the merging linkedlist.
        #p1 will represent the remaining portion of LinkedList 1 and p2 will do that for LinkedList2
        
        #assigning p1 and p2 to heads of L1 and L2 initially
        p1 = l1 
        p2 = l2 
        
        #If one of the linkedlist is empty
        if l1 == None:
            return l2
        if l2 == None : 
            return l1
        
        #Note : we are going to make the merging process in-place
        
        #WE WILL DETERMINE THE OVERALL HEAD OF THE MERGED LINKEDLIST AND TAIL OF THE MERGING LINKEDLIST
        #AND MOVE OUR POINTERS ACCORDINGLY
        if p1.val <= p2.val:
            head = l1
            tail = l1 
            p1 = p1.next
        else:
            head = l2
            tail = l2
            p2 = p2.next
        
        #NOW, WE WILL SET OUR TERMINAL CONDITION AND TRAVERSE OVER THE LINKEDLIST
        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next 
            else:
                tail.next = p2
                p2 = p2.next 
            tail = tail.next
        
        #fFINAL PIECE WHERE WE WILL SIMPLY LINK THE REMAINING PORTION OF LINKEDLIST WHICH HAS NOT BEEN COMPLETELY TRAVERSED YET
        if p1 == None:
            tail.next = p2 
        if p2 == None:
            tail.next = p1
        return head
            
            