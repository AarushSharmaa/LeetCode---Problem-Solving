# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #O(N) Time and O(1) Space
        
        """
        from collections import OrderedDict
        d = OrderedDict()
        #d = {}
        current = head
        while current:
            if current in d:
                return True
            else:
                d[current] = 0
                current = current.next
        return False
        """
        
        #O(N) Time and O(1) Space
        
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        """
        
        d = {}
        temp = head
        while temp:
            if temp in d:
                return True
            else:
                d[temp] = 1
                temp = temp.next
        return False