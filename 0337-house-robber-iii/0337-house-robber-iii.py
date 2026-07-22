# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)
            l0, l1 = dfs(node.left)
            r0, r1 = dfs(node.right)
            take = node.val + l0 + r0
            skip = max(l0, l1) + max(r0, r1)
            return (skip, take)

        skip, take = dfs(root)
        return max(skip, take)