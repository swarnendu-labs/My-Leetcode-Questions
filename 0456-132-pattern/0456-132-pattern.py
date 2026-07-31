class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float("-inf")
        for x in reversed(nums):
            if x < third:
                return True
            while stack and stack[-1] < x:
                third = stack.pop()
            stack.append(x)
        return False