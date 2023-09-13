# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        # space slow and fast apart by k
        for i in range(k):
            if fast.next:
                fast = fast.next
            else:
                fast = head
        # iterate until fast reaches the head
        # slow will be the location of the new tail
        while fast.next:
            slow = slow.next
            fast = fast.next
        # slow = new_tail
        # slow.next = new_head
        new_head = None
        if slow.next:
            new_head = slow.next
        else:
            # new_head would equal original head, no rotation required
            return head
        slow.next = None
        fast.next = head
        return new_head
        