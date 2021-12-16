# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #O(N) Time and O(N) Space
        #Using Stack
        
        """
        stack = []
        temp = head
        
        #In first traversal, we will push all the elements of linkedlist to the stack
        while temp:
            stack.append(temp.val)
            temp = temp.next
        count = 0 

        #In second traversal, we will iterate over the linkedlist and match them with the top of the stack
        #if it matches, pop them and continue traversal. If it does not, return False
        while head:
            element = stack.pop()
            if element == head.val:
                head = head.next
                count += 1
            else:
                return False
        #if False is not returned
        #it means all elements got removed from stack and linkedlist is a palindrome
        #so, we will return True
        return True
        """
        
        #We will now aim to do it in O(N) Time and O(1) Space
        #can we revert the second half - for eg. if we have a linkedlist that is
        #1->0->3->0->1 and if we revert the second half, it becomes 1 -> 0 -> 3 <- 0 <- 1
        #and then, we can use 2 pointers, one starting at head and other starting at tail
        #and match values from head and tail. If a value do not match, return False as it will never make a
        #Palindromic LinkedList
        
        #now, we need two things : first, to find the middle point
        #then, to revert the second half of linkedlist starting from the middle point till en
        #at last, one traversal using two pointers, one from front and other from tail to check if
        #it is a Palindrome or not
        
        #LET US FIND THE MIDDLE NODE NOW
        
        slow = head
        fast = head
        # find the mid node - which will be represented by slow 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #LET US NOW REVERT THE SECOND HALF OF THE LINKEDLIST STARTING FROM THE BEGINNING
        
        #slow will now represent the middle node of the linkedlist
        #reverse the second half starting from the middle node
        current = slow
        previous = None
        while current: #for this remaining linkedlist, current will act as the head
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        #for the reverted linkedlist, previous will act as the head
        
        
        #compare the first and second half of the LINKEDLIST
        
        #head will continue to be the head of first half of the linkedlist
        #previous will hold the head of the reverted linkedlist
        tail = previous
        while head != None and tail != None : # while node and head:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        return True
        
       