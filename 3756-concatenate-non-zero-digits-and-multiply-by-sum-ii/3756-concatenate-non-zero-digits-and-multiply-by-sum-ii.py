from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(s)

        val = [0] * (n + 1)
        sm = [0] * (n + 1)
        cnt = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = int(ch)
            val[i + 1] = val[i]
            sm[i + 1] = sm[i]
            cnt[i + 1] = cnt[i]

            if d != 0:
                val[i + 1] = (val[i] * 10 + d) % mod
                sm[i + 1] = sm[i] + d
                cnt[i + 1] = cnt[i] + 1

        power = [1] * (n + 1)

        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 10) % mod

        ans = []

        for l, r in queries:
            k = cnt[r + 1] - cnt[l]
            x = (val[r + 1] - val[l] * power[k]) % mod
            digit_sum = sm[r + 1] - sm[l]
            ans.append((x * digit_sum) % mod)

        return ans