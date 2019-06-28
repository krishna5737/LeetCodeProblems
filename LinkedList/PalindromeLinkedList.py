# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseLinkedList(self,head):
        previous = None
        current = head
        while(current):
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

    def find_prev(self,ptr,head):
        while(head.next!=ptr):
            head = head.next
        return head
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(not head):
            return True 
        if(not head.next):
            return True
        if(not head.next.next):
            if(head.val == head.next.val):
                return True
            return False
        
        slow_ptr = head
        fast_ptr = head
        while(fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if(fast_ptr):
            number = 1
            ptr_mid = slow_ptr
        else:
            number = 0
            mid = slow_ptr
            ptr_mid = self.find_prev(mid,head)
        ptr_mid.next = self.reverseLinkedList(ptr_mid.next)
        test = ptr_mid.next
        while(test):
            print(test.val, head.val)
            if(test.val != head.val):
                return False
            test = test.next
            head = head.next
        return True    

        
