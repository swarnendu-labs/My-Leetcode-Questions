from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = list(set(nums))
        M = 2048

        pair = [False] * M
        for a in vals:
            for b in vals:
                pair[a ^ b] = True

        ans = [False] * M
        for p in range(M):
            if pair[p]:
                for v in vals:
                    ans[p ^ v] = True

        return sum(ans)