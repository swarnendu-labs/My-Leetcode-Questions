from typing import List

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix = [0]
        s = 0

        for x in nums:
            s += 1 if x == target else -1
            prefix.append(s)

        vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = Fenwick(len(vals))
        ans = 0

        for p in prefix:
            ans += bit.query(rank[p] - 1)
            bit.update(rank[p], 1)

        return ans