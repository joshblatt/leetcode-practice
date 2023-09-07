# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(n) time O(n) space
# Recursive + DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)

            temp = root.right
            root.right = root.left
            root.left = temp
            return root
        return None