from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, current_num):
            if not node:
                return 0

            current_num = current_num * 10 + node.val

            # Leaf node
            if not node.left and not node.right:
                return current_num

            left_sum = dfs(node.left, current_num)
            right_sum = dfs(node.right, current_num)

            return left_sum + right_sum

        return dfs(root, 0)