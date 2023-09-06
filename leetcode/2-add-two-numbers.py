# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time O(n) space
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur_node = None
        prev_node = None
        carry_over = 0
        while l1 is not None or l2 is not None or carry_over != 0:
            cur_node = ListNode()
            if head is None:
                head = cur_node
            if prev_node is not None:
                prev_node.next = cur_node
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            cur_node.val = (l1_val + l2_val + carry_over) % 10
            carry_over = floor((l1_val + l2_val + carry_over) / 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            prev_node = cur_node
        return head

