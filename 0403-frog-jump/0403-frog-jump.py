class Solution:
    def canCross(self, stones):
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        stone_set = set(stones)

        for stone in stones:
            for k in dp[stone]:
                for jump in (k - 1, k, k + 1):
                    if jump > 0 and stone + jump in stone_set:
                        dp[stone + jump].add(jump)

        return len(dp[stones[-1]]) > 0