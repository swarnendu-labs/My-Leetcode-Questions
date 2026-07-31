# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return None

        vals = list(map(int, data.split(",")))
        i = 0

        def build(low, high):
            nonlocal i
            if i == len(vals):
                return None
            v = vals[i]
            if v < low or v > high:
                return None
            i += 1
            node = TreeNode(v)
            node.left = build(low, v)
            node.right = build(v, high)
            return node

        return build(float("-inf"), float("inf"))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans