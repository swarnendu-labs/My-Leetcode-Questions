from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)
        freq = [0] * (m + 1)
        for x in nums:
            freq[x] += 1

        divcnt = [0] * (m + 1)
        for d in range(1, m + 1):
            s = 0
            for k in range(d, m + 1, d):
                s += freq[k]
            divcnt[d] = s

        exact = [0] * (m + 1)
        for d in range(m, 0, -1):
            c = divcnt[d]
            pairs = c * (c - 1) // 2
            k = d * 2
            while k <= m:
                pairs -= exact[k]
                k += d
            exact[d] = pairs

        pref = []
        vals = []
        cur = 0
        for g in range(1, m + 1):
            if exact[g]:
                cur += exact[g]
                pref.append(cur)
                vals.append(g)

        return [vals[bisect_right(pref, q)] for q in queries]