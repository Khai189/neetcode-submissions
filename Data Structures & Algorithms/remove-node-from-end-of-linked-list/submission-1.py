# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        k = n
        while curr and k > 0:
            print(curr.val)
            curr = curr.next
            k-=1
        
        sentinel = ListNode(0, head)
        prev = sentinel

        while curr:
            curr = curr.next
            prev = prev.next
        
        prev.next = prev.next.next
        return sentinel.next


        