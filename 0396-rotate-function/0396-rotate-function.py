class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)

        total = sum(nums)

        f = 0
        for i, num in enumerate(nums):
            f += i * num

        ans = f

        for i in range(1, n):
            f = f + total - n * nums[n - i]
            ans = max(ans, f)

        return ans