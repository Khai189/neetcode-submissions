# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        current = head
        dummy = ListNode(0, head)
        prev = dummy
        while current and n > 0:
            n-=1
            current = current.next
        while current:
            current = current.next
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next
    
       
        

        

