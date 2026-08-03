class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nxt = {}
        for x in nums2:
            while stack and stack[-1] < x:
                nxt[stack.pop()] = x
            stack.append(x)
        while stack:
            nxt[stack.pop()] = -1
        return [nxt[x] for x in nums1]