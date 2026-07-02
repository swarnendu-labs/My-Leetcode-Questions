# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        ans = []
        path = []

        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and remaining == node.val:
                ans.append(path[:])
            else:
                dfs(node.left, remaining - node.val)
                dfs(node.right, remaining - node.val)

            path.pop()

        dfs(root, targetSum)
        return ans