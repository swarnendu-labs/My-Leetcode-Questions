from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        ugly = [1] * n
        idx = [0] * m
        vals = primes[:]

        for i in range(1, n):
            nxt = min(vals)
            ugly[i] = nxt
            for j in range(m):
                if vals[j] == nxt:
                    idx[j] += 1
                    vals[j] = primes[j] * ugly[idx[j]]

        return ugly[-1]