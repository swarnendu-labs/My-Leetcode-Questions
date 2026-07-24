class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(2, n + 1):
            for l in range(1, n - length + 2):
                r = l + length - 1
                dp[l][r] = float("inf")
                for x in range(l, r + 1):
                    dp[l][r] = min(dp[l][r], x + max(dp[l][x - 1], dp[x + 1][r]))

        return dp[1][n]