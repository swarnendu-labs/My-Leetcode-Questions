from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def dfs(mask, total):
            for i in range(1, maxChoosableInteger + 1):
                if not (mask >> i) & 1:
                    if total + i >= desiredTotal:
                        return True
                    if not dfs(mask | (1 << i), total + i):
                        return True
            return False

        return dfs(0, 0)