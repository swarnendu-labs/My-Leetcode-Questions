from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        a %= mod
        res = 1
        for d in b:
            res = pow(res, 10, mod) * pow(a, d, mod) % mod
        return res