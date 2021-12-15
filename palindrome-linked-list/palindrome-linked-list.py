# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:\
        
        #O(N) Time and O(N) Space
        #Using Stack
        
        stack = []
        temp = head
        
        #In first traversal, we will push all the elements of linkedlist to the stack
        while temp:
            stack.append(temp.val)
            temp = temp.next
            
        #In second traversal, we will iterate over the linkedlist and match them with the top of the stack
        #if it matches, pop them and continue traversal. If it does not, return False
        while head:
            element = stack.pop()
            if element == head.val:
                head = head.next
            else:
                return False
        return True
    
        
            