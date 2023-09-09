# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        merged_list_head = ListNode()
        cur_node = merged_list_head
        prev_node = None
        while list1 is not None or list2 is not None:
            if list1 is None or list2 is None:
                if list1 is None:
                    cur_node.val = list2.val
                    list2 = list2.next
                else:
                    cur_node.val = list1.val
                    list1 = list1.next
            elif list1.val < list2.val:
                cur_node.val = list1.val
                list1 = list1.next
            else:
                cur_node.val = list2.val
                list2 = list2.next
            if prev_node is not None:
                prev_node.next = cur_node

            prev_node = cur_node
            cur_node = ListNode()
        return merged_list_head

        