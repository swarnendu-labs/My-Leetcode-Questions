from bisect import bisect_left
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []
        for _, h in envelopes:
            i = bisect_left(lis, h)
            if i == len(lis):
                lis.append(h)
            else:
                lis[i] = h
        return len(lis)