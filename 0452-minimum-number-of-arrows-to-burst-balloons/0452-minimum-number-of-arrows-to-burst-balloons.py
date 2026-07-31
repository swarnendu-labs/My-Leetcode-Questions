class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ans = 0
        end = -float("inf")
        for s, e in points:
            if s > end:
                ans += 1
                end = e
        return ans