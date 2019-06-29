#Write a function that moves the last element to the front in a given Singly Linked List.
#For example, if the given Linked List is 1->2->3->4->5, 
#then the function should change the list to 5->1->2->3->4.

class Solution(object):
    def removeNthFromEnd(self, head):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        if(not head or not head.next):
            return head
        while(temp.next.next):
            temp = temp.next
            
        newHead = temp.next
        newHead.next = head
        temp.next = None
        return newHead
