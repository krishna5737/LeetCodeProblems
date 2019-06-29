# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        if(not head or not head.next):
            return head
        flag = 0
        deletingVal = temp.val
        deletingNode = temp
        while(temp):
            if(temp.val == deletingVal):
                flag = 1
            elif(flag == 1 and deletingVal != temp.val):
                flag = 0
                deletingNode.next = temp
                deletingVal = temp.val
                deletingNode = temp
            else:
                flag = 1
                deletingVal = temp.val
                deletingNode = temp
            temp = temp.next
        deletingNode.next = None
        return head                    
