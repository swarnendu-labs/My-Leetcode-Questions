from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):
        starts = sorted((x[0], i) for i, x in enumerate(intervals))
        vals = [x[0] for x in starts]
        ans = []
        for s, e in intervals:
            k = bisect_left(vals, e)
            ans.append(starts[k][1] if k < len(starts) else -1)
        return ans