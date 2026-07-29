"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        def dfs(node):
            cur = node
            last = None

            while cur:
                nxt = cur.next

                if cur.child:
                    child_head = cur.child
                    child_tail = dfs(child_head)

                    cur.next = child_head
                    child_head.prev = cur
                    cur.child = None

                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    last = child_tail
                else:
                    last = cur

                cur = nxt

            return last

        dfs(head)
        return head