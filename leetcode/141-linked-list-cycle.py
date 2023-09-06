# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) time O(n) space
# hashmap solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        visited = {}
        visited[head] = True
        cur_node = head
        while cur_node.next is not None:
            cur_node = cur_node.next
            if visited.get(cur_node):
                return True
            else:
                visited[cur_node] = True
        return False

# O(n) time O(1) space
# Using fast and slow pointers, we can figure out if there is a cycle
# If fast reaches the end without meeting up with the slow pointer, there is not a cycle
# Otherwise there must be a cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
