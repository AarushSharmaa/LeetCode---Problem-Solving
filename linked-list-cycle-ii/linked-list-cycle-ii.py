# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Approach 1 : Hashtable Approach - O(N) Time and O(N) Space
        #here, we are using a hashtable to store nodes corresponding to any random value (here, we have used  0 as value and nodes as keys)
        #and traversing over the linkedlist. if we find any node to be repeated again, we can say it is the first node
        #of the loop.
        
        """
        d = {}
        current = head
        while current:
            if current in d:
                return current 
            else:
                d[current] = 0 
                current = current.next
        return None
        """
        
        #Approach 2 :  Two Pointers Approach : Complexity Analysis : O(N^2) Time and O(1) Space
        #first, we will check if there is a cycle or not
        #if there is not a cycle, we will return Null
        #if there is a cycle, we will play around with pointers
        
        slow = head
        fast = head
        iscycle = False #this means that there is no cycle present
        #we will use this iscycle variable to check if we have a cycle or not
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #it means we have a cycle
                iscycle = True
                break 
                
        if iscycle == False: #it means if there is no cycle
            return None
        
        else: #it means we have a cycle and at some point, slow == fast
            #now, we will continously revolve this slow variable inside the loop
            #and at the same time, initialise a variable to head node
            p = head
            while 1: #while the statement is True 
                temp = slow #or fast
                #we will now continously revolve in the loop till we get temp == p
                while temp != p: 
                    temp = temp.next
                    if temp == slow:
                        break
                if temp == p:
                    return temp #or p 
                p = p.next
        