class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(-9999999) 
        temp = result
        while(l1 and l2):
            if(l2.val > l1.val):
                result.next = l1
                result = result.next
                l1 = l1.next
            else:
                result.next = l2
                result = result.next
                l2 = l2.next
        while(l1):
            result.next = l1
            result = result.next
            l1 = l1.next
            
        while(l2):
            result.next = l2
            result = result.next
            l2 = l2.next            
        temp = temp.next
        return temp
