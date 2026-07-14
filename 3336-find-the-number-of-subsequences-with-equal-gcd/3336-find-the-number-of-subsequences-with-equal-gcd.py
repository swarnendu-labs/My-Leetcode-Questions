from math import gcd

MOD = 10 ** 9 + 7

class Solution:
    def subsequencePairCount(self, nums):
        m = max(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [row[:] for row in dp]
            for g1 in range(m + 1):
                for g2 in range(m + 1):
                    v = dp[g1][g2]
                    if not v:
                        continue
                    ng1 = x if g1 == 0 else gcd(g1, x)
                    ng2 = x if g2 == 0 else gcd(g2, x)
                    ndp[ng1][g2] = (ndp[ng1][g2] + v) % MOD
                    ndp[g1][ng2] = (ndp[g1][ng2] + v) % MOD
            dp = ndp

        ans = 0
        for g in range(1, m + 1):
            ans = (ans + dp[g][g]) % MOD
        return ans 