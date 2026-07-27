class Solution:
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for x in nums:
            for j in range(target, x - 1, -1):
                dp[j] = dp[j] or dp[j - x]
        return dp[target]