from bisect import bisect_left, insort
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        if m > n:
            matrix = [list(row) for row in zip(*matrix)]
            m, n = n, m

        ans = -10**9

        for top in range(m):
            col = [0] * n
            for bottom in range(top, m):
                for c in range(n):
                    col[c] += matrix[bottom][c]

                prefix = 0
                s = [0]
                for x in col:
                    prefix += x
                    i = bisect_left(s, prefix - k)
                    if i < len(s):
                        ans = max(ans, prefix - s[i])
                    insort(s, prefix)

        return ans