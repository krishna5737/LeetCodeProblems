# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None or head.next == None):
            return head
        previous = head
        current = previous.next 
        next = current.next
        current.next = previous
        previous.next = next
        previous.next = self.swapPairs(next)
        return current
