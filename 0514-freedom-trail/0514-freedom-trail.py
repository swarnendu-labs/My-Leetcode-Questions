from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos = defaultdict(list)
        n = len(ring)

        for i, c in enumerate(ring):
            pos[c].append(i)

        @lru_cache(None)
        def dfs(i, cur):
            if i == len(key):
                return 0
            ans = float("inf")
            for nxt in pos[key[i]]:
                d = abs(nxt - cur)
                step = min(d, n - d)
                ans = min(ans, step + 1 + dfs(i + 1, nxt))
            return ans

        return dfs(0, 0)