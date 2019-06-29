#Given a Singly Linked List, starting from the second node delete all alternate nodes of it. 
#For example, if the given linked list is 1->2->3->4->5 then your function should convert it to 1->3->5, 
#and if the given linked list is 1->2->3->4 then convert it to 1->3.

def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        count = 1
        p1 = head
        while(head and head.next):
            if(count%2!=0):
                head.next = head.next.next
                count+=2
                head = head.next
            else:
                head = head.next
                count+=1
        return p1
    
