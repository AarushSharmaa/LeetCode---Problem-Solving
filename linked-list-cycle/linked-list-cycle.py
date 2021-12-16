# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        from collections import OrderedDict
        #d = OrderedDict()
        d = {}
        current = head
        while current:
            if current in d:
                return True
            else:
                d[current] = 0
                current = current.next
        return False
        