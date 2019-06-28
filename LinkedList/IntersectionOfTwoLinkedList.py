# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLLlength(self,head):
        temp = head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count 
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = self.getLLlength(headA)
        l2 = self.getLLlength(headB)
        absdiff = abs(l1-l2)
        if(l1>l2):
            while(absdiff):
                headA =  headA.next
                absdiff-=1
            # print(headA.val)
        if(l2>l1):
            while(absdiff):
                headB =  headB.next
                absdiff-=1
        while((headA and headB) and headB != headA):
            print(headA.val,headB.val)
            headA = headA.next
            headB = headB.next
        if(headA):
            return headA
        else:
            return null
