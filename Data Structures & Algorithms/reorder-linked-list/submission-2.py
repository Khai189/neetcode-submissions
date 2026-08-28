# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        l1 = head
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        end = slow.next
        slow.next = None

        prev = None
        curr = end
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l2 = prev

        while l2:
            temp1, temp2 = l1.next, l2.next
            
            l1.next = l2
            l2.next = temp1
            
            l1, l2 = temp1, temp2





           

        

