# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Sentinel removes edge case where the first element is a repeat
# Single pass O(n) time O(1) space
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        pred = sentinel
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return sentinel.next
            

