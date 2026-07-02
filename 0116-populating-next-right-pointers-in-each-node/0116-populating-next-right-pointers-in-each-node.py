"""
# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            curr = leftmost

            while curr:
                curr.left.next = curr.right

                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next

            leftmost = leftmost.left

        return root