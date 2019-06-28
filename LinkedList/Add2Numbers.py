#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order and each of their nodes contain a single digit. 
#Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        sum = l1.val+l2.val
        carry = sum //10
        sum = sum%10
        l = ListNode(sum)
        p = l
        l1 = l1.next
        l2 = l2.next
        
        while(l1 and l2):
            sum = l1.val+l2.val + carry 
            carry = sum //10
            sum = sum%10
            l.next = ListNode(sum)
            l1 = l1.next
            l2 = l2.next
            l = l.next
        while(l1):
            sum = l1.val+ carry 
            carry = sum //10
            sum = sum%10
            l.next = ListNode(sum)
            l1 = l1.next
            l = l.next
        while(l2):
            sum = l2.val+ carry 
            carry = sum //10
            sum = sum%10
            l.next = ListNode(sum)
            l2 = l2.next
            l = l.next
        if(carry == 1):
            l.next = ListNode(1)
        return p
        
        
        
