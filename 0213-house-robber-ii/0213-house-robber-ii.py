class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def solve(arr):
            prev = curr = 0
            for x in arr:
                prev, curr = curr, max(curr, prev + x)
            return curr

        return max(solve(nums[:-1]), solve(nums[1:]))