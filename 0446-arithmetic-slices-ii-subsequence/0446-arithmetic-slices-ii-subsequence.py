from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = dp[j][d]
                ans += cnt
                dp[i][d] += cnt + 1

        return ans