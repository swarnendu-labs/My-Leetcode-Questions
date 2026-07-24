# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        ans = node.val
        i = 1
        while node:
            if random.randrange(i) == 0:
                ans = node.val
            node = node.next
            i += 1
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()