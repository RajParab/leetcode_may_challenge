"""
Explanation

"""

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next==None or head.next.next==None):
            return head
        odd=head
        even=head.next
        evenFirst=even
        
        while(even and even.next):
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
            
        odd.next=evenFirst
        
        return head
