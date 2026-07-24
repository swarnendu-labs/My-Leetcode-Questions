from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count(x):
            i, j = n - 1, 0
            c = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= x:
                    c += i + 1
                    j += 1
                else:
                    i -= 1
            return c

        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo