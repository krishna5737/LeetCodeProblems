# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list
#where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(head == None or head.next == None or head.next.next == None):
            return False
        else:
            slow_ptr = head
            fast_ptr = head
            while(fast_ptr.next):
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
                if(slow_ptr == fast_ptr):
                    return True
                if(slow_ptr == None or fast_ptr.next == None or fast_ptr.next.next == None):
                    return False
                
