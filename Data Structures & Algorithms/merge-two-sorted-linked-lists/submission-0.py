# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == [] and list2 == []:
            return []

        l1_pointer = list1
        l2_pointer = list2
        head = ListNode(float("-infinity"))
        current = head
        while l1_pointer and l2_pointer:          
            if l1_pointer.val > l2_pointer.val:
                current.next = ListNode(l2_pointer.val)
                l2_pointer = l2_pointer.next
                current = current.next
            else:
                current.next = ListNode(l1_pointer.val)
                l1_pointer = l1_pointer.next
                current = current.next
        current.next = l1_pointer if l1_pointer else l2_pointer


        head = head.next
        return head

        