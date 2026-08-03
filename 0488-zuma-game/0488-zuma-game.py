from functools import lru_cache
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def shrink(s):
            while True:
                i = 0
                t = []
                changed = False
                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        changed = True
                    else:
                        t.append(s[i:j])
                    i = j
                if not changed:
                    return s
                s = "".join(t)

        cnt = Counter(hand)
        colors = "RYBGW"

        @lru_cache(None)
        def dfs(b, r, y, b1, g, w):
            if not b:
                return 0
            balls = {'R': r, 'Y': y, 'B': b1, 'G': g, 'W': w}
            ans = float("inf")
            for i in range(len(b) + 1):
                for c in colors:
                    if balls[c] == 0:
                        continue
                    if i > 0 and b[i - 1] == c:
                        continue
                    if (i < len(b) and b[i] == c) or (0 < i < len(b) and b[i - 1] == b[i] != c):
                        nb = shrink(b[:i] + c + b[i:])
                        nballs = balls.copy()
                        nballs[c] -= 1
                        res = dfs(nb, nballs['R'], nballs['Y'], nballs['B'], nballs['G'], nballs['W'])
                        if res != float("inf"):
                            ans = min(ans, res + 1)
            return ans

        res = dfs(board, cnt['R'], cnt['Y'], cnt['B'], cnt['G'], cnt['W'])
        return -1 if res == float("inf") else res