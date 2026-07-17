from typing import List
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def solve(exp):
            res = []
            for i, c in enumerate(exp):
                if c in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i + 1:])
                    for a in left:
                        for b in right:
                            if c == "+":
                                res.append(a + b)
                            elif c == "-":
                                res.append(a - b)
                            else:
                                res.append(a * b)
            if not res:
                res.append(int(exp))
            return res

        return solve(expression)