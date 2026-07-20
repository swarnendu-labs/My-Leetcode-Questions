from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + [x for x in nums if x > 0] + [1]
        m = len(arr)
        dp = [[0] * m for _ in range(m)]

        for length in range(2, m):
            for left in range(m - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k] + dp[k][right] + arr[left] * arr[k] * arr[right]
                    )

        return dp[0][m - 1]